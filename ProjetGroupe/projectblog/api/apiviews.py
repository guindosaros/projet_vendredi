from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters

from blog.models import *
from contact.models import *
from configuration.models import *
from .models import *

from .serializers import CategorieSerializer, TagSerializer, ArticleSerializer, LikeSerializer, NewsletterSerializer, ContactSerializer

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# class CommentaireViewSet(viewsets.ModelViewSet):
#     queryset = Commentaire.objects.all()
#     serializer_class = CommentaireSerializer
    
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
