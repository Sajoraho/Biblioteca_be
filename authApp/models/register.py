from django.db import models
from django.db.models.deletion import CASCADE
from .user import User
class Register(models.Model):

    ROLE_CHOOSE = (
        ('Administrador','Administrador'),
        ('Bibliotecario','Bibliotecario'),
        ('Estudiante','Estudiante'),
    )

    id = models.BigAutoField(primary_key=True)
    institution = models.CharField('Institution', max_length = 60)
    address = models.CharField('Address', max_length = 30)
    telephone = models.CharField('Telephone', max_length = 30)
    role_choose = models.CharField(max_length=30, choices=ROLE_CHOOSE)
    user = models.ForeignKey(User, related_name='register', on_delete=models.CASCADE)