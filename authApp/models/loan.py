from django.db import models
from .book import Book
from .user import User

class Loan(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_borrow = models.DateTimeField
    date_agreed = models.DateTimeField
    date_return = models.DateTimeField
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

