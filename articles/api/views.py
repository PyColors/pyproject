# Clean syntax with viewsets from https://www.django-rest-framework.org/api-guide/viewsets/
from rest_framework import viewsets

from articles.models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     UpdateAPIView,
#     DestroyAPIView,
# )


# # Get views - (https://www.django-rest-framework.org/api-guide/generic-views/#listapiview)
# class ArticleListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# # Post - (https://www.django-rest-framework.org/api-guide/generic-views/#createapiview)
# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# # Update - (https://www.django-rest-framework.org/api-guide/generic-views/#updateapiview)
# class ArticleUpdateView(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# # Delete - (https://www.django-rest-framework.org/api-guide/generic-views/#destroyapiview)
# class ArticleDeleteView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
