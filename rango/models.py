from operator import truediv
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default= 0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    website = models.URLField(max_length=500, blank = True)
    picture = models.ImageField(blank = True, upload_to = 'profile_pictures')
    def __str__(self):
        return self.user.username