from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

from rest_framework.routers import DefaultRouter

from .apiviews import CategorieViewSet, TagViewSet, ArticleViewSet, LikeViewSet, NewsletterViewSet, ContactViewSet


router = DefaultRouter()
router.register('categorie', CategorieViewSet, base_name='categorie')
router.register('tag', TagViewSet, base_name='tag')
router.register('article', ArticleViewSet, base_name='article')
router.register('like', LikeViewSet, base_name='like')
router.register('Contact', ContactViewSet, base_name='Contact')
router.register('newsletter', NewsletterViewSet, base_name='newsletter')

urlpatterns = [
 
]

urlpatterns += router.urls
