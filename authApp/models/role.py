from django.db import models 

class Role(models.Model):
    ROLE_CHOOSE = (
        ('Administrador','Administrador'),
        ('Bibliotecario','Bibliotecario'),
        ('Estudiante','Estudiante'),
    )
    
    id = models.BigAutoField(primary_key=True)
    role_choose = models.CharField(max_length=30, choices=ROLE_CHOOSE)