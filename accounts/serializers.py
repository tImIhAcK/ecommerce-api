from rest_framework import serializers
from accounts.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)

        token['email'] = user.email
        token['full_name'] = user.full_name
        token['phone_number'] = str(user.phone_number)
        token['email_verified']= user.email_verified
        token['fullname'] = str(user.get_full_name())
        
        return token

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(max_length=120, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password',)
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
class LoginSerializer(serializers.ModelSerializer):
     password = serializers.CharField(max_length=120, min_length=6, write_only=True)
     
     class Meta:
        model = User
        fields = {'email', 'password', 'token'}
        read_only_fields = ['token',]