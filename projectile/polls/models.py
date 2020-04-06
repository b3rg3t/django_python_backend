from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    '''Create a new question for polls app'''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') 
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        '''Ordering the returned data with the latest added question to the top'''
        ordering = ('-pub_date',)
    def __str__(self):
        return self.question_text
    

class Choice(models.Model):
    '''Create a new choice for a question'''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text