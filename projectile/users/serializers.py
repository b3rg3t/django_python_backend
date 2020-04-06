from rest_framework import serializers
from .models import userProfile
from django.contrib.auth.models import User

class userProfileSerializer(serializers.ModelSerializer):
    # user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = userProfile
        fields = ('description', 'location', 'date_joined', 'updated_on', 'is_organizer')
        
        
        
        
        


class UserSerializer(serializers.ModelSerializer):
    profile = userProfileSerializer()
    class Meta:
        model = User
        fields = '__all__'
    def update(self, instance, validated_data):
        email = validated_data.pop('email', "")
        profile = validated_data.pop('profile', "")
        first_name = validated_data.pop('first_name', "")
        last_name = validated_data.pop('last_name', "")
        username = validated_data.pop('username', instance.username)
        instance.first_name = first_name
        instance.last_name = last_name
        instance.username = username
        instance.email = email
        instance.save(update_fields = ['first_name', 'last_name', 'username', 'email'])
        instance.profile.location = profile['location']
        instance.profile.description = profile['description']
        instance.profile.save(update_fields = ['location', 'description'])
        return instance


