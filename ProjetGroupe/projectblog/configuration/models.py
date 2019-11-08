from django.db import models

# Create your models here.

class Social(models.Model):
    # TODO: Define fields here
    choice=[('FB','facebook'),('TW','twitter'),('INS','instagram'),('GOO','google')]
    name = models.CharField(max_length=100,choices=choice)
    lien = models.URLField(max_length=200)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    @property
    def font(self):
        if self.name == 'FB':
            font = 'icon-facebook'
        elif self.name == 'TW':
            font ='icon-twitter'
        elif self.name == 'INS':
            font ='icon-instagram"'
        elif self.name == 'GOO':
            font ='icon-google-plus'
        return font
    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"

    def __str__(self):
        return '{}'.format(self.name)


class Site(models.Model):
    """Model definition for Site."""
    logo = models.ImageField(upload_to='logo/')
    social = models.ForeignKey(Social, on_delete=models.CASCADE, related_name='site_social')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Site."""

        verbose_name = 'Site'
        verbose_name_plural = 'Sites'

class Front(models.Model):
    """Model definition for Front."""
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='config/')
    titre = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Front."""

        verbose_name = 'Front'
        verbose_name_plural = 'Fronts'

    def __str__(self):
        """Unicode representation of Front."""
        return self.nom
    

