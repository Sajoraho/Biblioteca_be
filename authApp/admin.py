from django.contrib import admin

from .models.user import User
from .models.register import Register
from .models.book import Book
from .models.loan import Loan

admin.site.register(User)
admin.site.register(Register)
admin.site.register(Book)
admin.site.register(Loan)

# Register your models here.
