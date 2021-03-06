from typing import List
from django.db import models
from random import sample
from random import choice

# Create your models here.
class Image(models.Model) :
    name = models.IntegerField()
    description = models.TextField()
    mode = models.CharField(max_length=255)
    celltype = models.CharField(max_length=255, null=True)
    components = models.CharField(max_length=255, null=True)
    doi = models.CharField(max_length=255)
    organism = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return str(self.name)

    @staticmethod
    def get_random_images(field, number):
        # rand_field = choice(list_of_distinct_field)
        result_list = []

        if field == 'mode':
            list_of_distinct_field = [i['answer'] for i in Answer.objects.filter(question_id=1).values()]
            for i in range(10):
                rand_field = choice(list_of_distinct_field)
                list_of_specific_field = list(Image.objects.filter(mode=rand_field))
                result_list.append({rand_field: sample(list_of_specific_field, number)})

        elif field == 'components':
            # this while loop is created to prevent that we have only one record in our list
            list_of_distinct_field = [i['answer'] for i in Answer.objects.filter(question_id=2).values()]
            for i in range(10):
                list_of_specific_field = [0]
                while len(list_of_specific_field) == 1:
                    rand_field = choice(list_of_distinct_field)
                    list_of_specific_field = list(Image.objects.filter(components=rand_field))
                result_list.append({rand_field: sample(list_of_specific_field, number)})
      
        return result_list
    
    @staticmethod
    def get_metadatas():
        metadatas_list = []
        fields = ['mode', 'components', 'celltype', 'organism']
        for field in fields:
            metadatas_list += [i[field] for i in list(Image.objects.order_by().values(field).distinct())]
        metadatas_list.remove('None')
        return metadatas_list

class Question(models.Model):
    question = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    imagefield = models.ManyToManyField(Image)
    points = models.IntegerField()
    n_answer = models.IntegerField()
    n_image = models.IntegerField()

    def __str__(self) -> str:
        return self.question

class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    definition = models.TextField()

    def __str__(self) -> str:
        return self.answer
    
    # a static function to generate random answers 
    @staticmethod
    def generate_random_answers(idd):
        list_of_answers = [i['answer'] for i in Answer.objects.filter(question_id=idd).values()]
        return sample(list_of_answers, 4)
