from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        # specify ar
        model = Article
        fields = ('title', 'content')