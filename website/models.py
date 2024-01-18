from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Profile(models.Model):
    name = models.TextField()
    logo = models.ImageField(upload_to='profile/logo/', blank=True,null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Profile, self).save(*args, **kwargs)
    
class Link(models.Model):
    class Type_Menu(models.TextChoices):
        FOOD = "1", "Food"
        DRINKS = "2", "Drinks/Bar"

    linktype = models.CharField(choices=Type_Menu.choices, default=Type_Menu.FOOD, max_length=100)
    title = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.profile.name} - Link {self.id}"
