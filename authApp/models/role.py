from django.db import models

class Role(models.Model):
    ROLE_CHOOSE = (
        ('AD','Administrador'),
        ('BI','Bibliotecario'),
        ('ES','Estudiante'),
    )
    
    id = models.BigAutoField(primary_key=True)
    role_choose = models.CharField(max_length=2, choices=ROLE_CHOOSE)