from django.db import models
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    links = ArrayField(
        models.URLField(),
        blank=True,
        default=list,
        help_text="Add one or more URLs separated by commas."
    )
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    position = models.PositiveIntegerField(default=0, help_text="Lower numbers show first")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['position']

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name

