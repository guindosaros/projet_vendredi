from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class SocialAdmin(admin.ModelAdmin):

    list_display = ('name', 'lien', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class SiteAdmin(admin.ModelAdmin):

    list_display = ('logo', 'social', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )


class FrontAdmin(admin.ModelAdmin):

    list_display = (
        
        'nom',
        'image',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Social, SocialAdmin)
_register(models.Site, SiteAdmin)
_register(models.Front, FrontAdmin)
