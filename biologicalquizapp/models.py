from django.db import models

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
        return self.name

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
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    definition = models.TextField()

    def __str__(self) -> str:
        return self.answer
