from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce import HTMLField
from configuration.models import Social

class Profile(models.Model):

    # Appel de user
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # 1 user <---> 1 profil
    
    # Champs suplementaires
    
    contacts = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='profile/', default='useravatar.png')
    birth_date = models.DateField(null=True)

    # Initialisation a la creation
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        
        instance.profile.save()
        
    class class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class Tag(models.Model):
    nom = models.CharField(max_length=50)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nom



# Create your models here.

class Categorie(models.Model):
    nom=models.CharField(, max_length=50)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nom
    
    class class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    categorie=models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="categorie_article")
    auteur=models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="auteur_article")
    tag = models.ManyToManyField(Tag, related_name="tab_articles")
    titre=models.CharField(max_length=50)
    descriptions=models.TextField()
    images=models.ImageField(upload_to="Image",null=True)
    videos = models.URLField()
    contenue = HTMLField('Content')
    date_add=models.DateTimeField(auto_now_add=True)
    date_upd=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    
    def __str__(self):
        return self.titre
    
    class class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Like(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE ,related_name="user_like")
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_like")
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    
    class class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'


