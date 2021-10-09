from authApp.models.register import Register 
from rest_framework import serializers 
 
class RegisterSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Register 
        fields = ['id', 'institution', 'address', 'telephone', 'user', 'role_choose'] 