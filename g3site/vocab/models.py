import datetime
from django.db import models
from django.utils import timezone

class Word(models.Model):
    word_text = models.CharField(max_length=50)
    add_date = models.DateTimeField('date vocab added')
    def __str__(self):
        return self.word_text

    def add_date(self):
        return self.add_date
    
class Mean(models.Model):
    mean_text = models.CharField(max_length=200)
    type_text = models.CharField(max_length=10)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    add_date = models.DateTimeField('date vocab added')
    def __str__(self):
        return self.mean_text
        
    def add_date(self):
        return self.add_date