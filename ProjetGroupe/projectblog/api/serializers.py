from rest_framework import serializers

from blog.models import *
from contact.models import *
from configuration.models import *
from .models import *

from drf_dynamic_fields import DynamicFieldsMixin

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

# class CommentaireSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Commentaire
#         fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    article_like = LikeSerializer(many=True, required=False)
    class Meta:
        model = Article
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    tab_articles = ArticleSerializer(many=True, required=False)
    class Meta:
        model = Tag
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    categorie_article = ArticleSerializer(many=True, required=False)
    class Meta:
        model = Categorie
        fields = '__all__'

#=============== App ContactApp ==============#

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'