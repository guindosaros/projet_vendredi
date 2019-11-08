from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'comment',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('email',)
    list_filter = ('email',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)
_register(models.Newsletter, NewsletterAdmin)
