from django.contrib.auth.models import User





def create_profile(sender, instance, created, **kwargs):
    from .models import userProfile
    if created:
        userProfile.objects.create(user=instance)