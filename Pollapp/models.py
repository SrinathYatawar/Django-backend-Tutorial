from django.db import models



class Creator(models.Model):
    created_by = models.CharField(max_length=200)



class Question(models.Model):
    creator = models.ForeignKey(Creator,related_name='questions',on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField()



class Choices(models.Model):
    question = models.ForeignKey(Question,related_name='choices',on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    voteCount= models.IntegerField(default=0)