import uuid

from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe


# Create your models here.

class testimonial(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    date_posted = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class prayerRequest(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    date_posted = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class gallery(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    images = models.ImageField()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.image = None

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return str(self.images)


class event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    name = models.CharField(max_length=1000, null=True, blank=False)
    date = models.CharField(max_length=1000, null=True, blank=True)
    about = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return str(self.name)


class life_youtube(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.url)


class newsletter(models.Model):
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.email
