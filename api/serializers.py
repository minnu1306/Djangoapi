from .models import Article
from rest_framework import serializers

class ArticleSe(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'

    def create(self,validated_data):
        return Article.objects.create(validated_data)

    def update(self,instance,validated_data):
        instance.title=validated_data.get('title', instance.title)
        instance.author=validated_data.get('author', instance.author)
        instance.email=validated_data.get('email', instance.email)

        instance.save()
        return instance
