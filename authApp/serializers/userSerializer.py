from rest_framework import serializers 
from authApp.models.user import User 
from authApp.models.register import Register 
from authApp.serializers.registerSerializer import RegisterSerializer 
 
 
class UserSerializer(serializers.ModelSerializer): 
    register = RegisterSerializer() 
    class Meta: 
        model = User 
        fields = ['id', 'username', 'password', 'name', 'lastname', 'email', 'register'] 
 
    def create(self, validated_data): 
        registerData = validated_data.pop('register') 
        userInstance = User.objects.create(**validated_data) 
        Register.objects.create(user=userInstance, **registerData) 
        return userInstance 
 
    def to_representation(self, obj): 
        user = User.objects.get(id=obj.id) 
        register = Register.objects.get(user=obj.id)        
        return { 
            'id': user.id,  
            'username': user.username, 
            'password': user.password, 
            'name': user.name, 
            'lastname': user.lastname,
            'email': user.email,
            'register': { 
                    'id': register.id, 
                    'institution': register.institution, 
                    'address': register.address, 
                    'telephone': register.telephone,
                    'role': register.role_choose, 
            } 
        }