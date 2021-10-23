from django.db import models

# Create your models here.

# class Image(models.Model):
#     name = models.CharField(max_length=20)
#     description = models.TextField(unique=False)
#     mode = models.CharField(max_length=255)
#     celltype = models.CharField(max_length=255, null=True)
#     component = models.CharField(max_length=255, null=True)
#     doi = models.URLField()
#     organism = models.CharField(max_length=255, null=True)

# class Question(models.Model):
#     question = models.CharField(max_length=255)
#     type = models.CharField(max_length=255)
#     image_field = models.ForeignKey(Image, on_delete=models.CASCADE)
#     component_filed = models.ForeignKey(Image, on_delete=models.CASCADE)

# class Answer(models.Model):
#     question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    
#     # answer have two foreingkeys to the image table !!!!
#     answer = models.CharField(max_length=255)
#     definition = models.TextField()
