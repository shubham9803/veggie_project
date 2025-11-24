from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from .models import Profile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ('user','role','phone')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    role = serializers.ChoiceField(choices=Profile.ROLE_CHOICES, default='viewer', write_only=True)

    class Meta:
        model = User
        fields = ('username','email','password','first_name','last_name','role')

    def create(self, validated_data):
        role = validated_data.pop('role', 'viewer')
        user = User.objects.create_user(**{k:v for k,v in validated_data.items() if k!='role'})
        # profile auto-created by signal; set role
        user.profile.role = role
        user.profile.save()
        return user
