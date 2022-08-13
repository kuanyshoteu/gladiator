from rest_framework import serializers
from .models import Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["name", "group", "mail", "image", "color", "coins", "sum_of_coins"]