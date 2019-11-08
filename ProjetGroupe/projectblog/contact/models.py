from django.db import models

# Create your models here.

class Contact(models.Model):
    """Model definition for Contact."""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.name

class Newsletter(models.Model):
    """Model definition for Newsletter."""
    email = models.EmailField()
    # TODO: Define fields here

    class Meta:
        """Meta definition for Newsletter."""

        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
