from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    verify_password = serializers.CharField(write_only=True, style={"input_type": "password"})
    profile_picture = serializers.ImageField(required=False)  

    class Meta:
        model = User
        fields = ["email", "full_name", "dob", "gender", "phone_number", "address", "profile_picture", "password", "verify_password"]

    def validate(self, data):
        """Ensure password and verify_password match."""
        if data["password"] != data["verify_password"]:
            raise serializers.ValidationError({"verify_password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        """Use UserManager.create_user to handle password hashing."""
        validated_data.pop("verify_password") 
        password = validated_data.pop("password")

        user = User.objects.create_user(password=password, **validated_data)  
        return user
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ["email", "full_name", "dob", "gender", "phone_number", "address", "profile_picture", "password"]

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input-type':'password'},write_only=True)
    verify_password = serializers.CharField(max_length=255, style={'input-type':'password'},write_only=True)
    class Meta:
        fields=['password','verify_password']
    def validate(self,attrs):
        password= attrs.get('password')
        verify_password= attrs.get('verify_password')
        user=self.context.get('user')
        if password != verify_password:
            raise serializers.ValidationError({"verify_password": "Passwords do not match."})
        user.set_password(password)
        user.save()
        return attrs
    

