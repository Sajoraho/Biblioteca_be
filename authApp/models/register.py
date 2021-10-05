from django.db import models
from django.db.models.deletion import CASCADE
from .user import User
from .role import Role

class Register(models.Model):
    id = models.BigAutoField(primary_key=True)
    institution = models.CharField('Institution', max_length = 60)
    address = models.CharField('Adress', max_length = 30)
    telephone = models.CharField('Telephone', max_length = 30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)