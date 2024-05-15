from rest_framework import serializers
from .models import PostModel

class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)
    class Meta:
        model = PostModel
        fields = ['name','body']