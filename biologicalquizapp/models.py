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
        list_of_distinct_field = [i[field] for i in list(Image.objects.order_by().values(field).distinct())]
        rand_field = choice(list_of_distinct_field)
        if field == 'mode':
            list_of_specific_field = list(Image.objects.filter(mode=rand_field))
        elif field == 'components':
            # this while loop is created to prevent that we have only one record in our list
            list_of_specific_field = [0]
            while len(list_of_specific_field) == 1:
                list_of_specific_field = list(Image.objects.filter(components=rand_field))
                rand_field = choice(list_of_distinct_field)
        elif field == 'celltype':
            list_of_specific_field = [0]
            while len(list_of_specific_field) == 1:
                list_of_specific_field = list(Image.objects.filter(celltype=rand_field))
                rand_field = choice(list_of_distinct_field)
            

        return sample(list_of_specific_field, number)

class Question(models.Model):
    question = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    imagefield = models.CharField(max_length=255)
    points = models.IntegerField()
    n_answer = models.IntegerField()
    n_image = models.IntegerField()

    def __str__(self) -> str:
        return self.question

class Answer(models.Model):
    question_id = models.IntegerField()
    answer = models.CharField(max_length=255)
    definition = models.TextField()

    def __str__(self) -> str:
        return self.answer
