from authApp.models.register import Register 
from rest_framework import serializers 
 
class RegisterSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Register 
        fields = ['institution', 'address', 'telephone', 'role_choose'] 