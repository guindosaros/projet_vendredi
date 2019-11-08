from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'contacts', 'image', 'birth_date')
    list_filter = (
        'user',
       'birth_date',
        'user',
        'contacts',
       'image',
       'birth_date',
    )


class TagAdmin(admin.ModelAdmin):

    list_display = ('nom', 'date_add', 'date_upd', 'status')
    list_filter = (
        'date_add',
        'date_upd',
        'status',
    )


class CategorieAdmin(admin.ModelAdmin):

    list_display = ('nom', 'date_add', 'date_upd', 'status')
    list_filter = (
        'date_add',
        'date_upd',
        'status',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'categorie',
        'auteur',
        'images',
        'videos',
        'date_add',
        'date_upd',
        'status',
    )
    list_filter = (
        'categorie',
        'auteur',
        'date_add',
        'date_upd',
        'status',
    )
    raw_id_fields = ('tag',)


class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'user_id',
        'article_id',
        'date_add',
        'date_upd',
        'status',
    )
    list_filter = (
        'user_id',
        'article_id',
        'date_add',
        'date_upd',
        'status',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)
_register(models.Tag, TagAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Like, LikeAdmin)
