from django.db import models
from .book import Book
from .register import Register
class Loan(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_borrow = models.DateField()
    date_agreed = models.DateField()
    date_return = models.DateField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    register = models.ForeignKey(Register,on_delete=models.CASCADE)

