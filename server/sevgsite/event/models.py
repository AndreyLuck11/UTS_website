from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    url = models.URLField(max_length=200, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    date_of_event_start = models.DateField(null=False)
    date_of_event_end = models.DateField(null=False)
    image_url = models.ImageField(upload_to="images/%Y/%m/%d", blank=True, null=True)
    file_url = models.FileField(upload_to="files/%Y/%m/%d", blank=True, null=True)
    cat = models.ForeignKey('category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
