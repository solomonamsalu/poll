from email.policy import default
from django.db import models
from django.utils import timezone
class Questions(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.question_text
class Choice(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=230)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
