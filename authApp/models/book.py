from django.db import models

class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField('Title', max_length = 90)
    author = models.CharField('Author', max_length = 90)
    language = models.CharField('Language', max_length = 30)
    year = models.DateField('Year')
    publisher = models.CharField('Publisher', max_length = 30)
    genre = models.CharField('Genre', max_length = 60)
    number = models.IntegerField('Version', default=1)




