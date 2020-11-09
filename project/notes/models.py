from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(
        upload_to='documents/%Y/%m/%d/', default='blank')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-Doc-detail', kwargs={'pk': self.pk})


class Video(models.Model):
    caption = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    video = models.FileField(
        upload_to='videos/%Y/%m/%d/', default='blank')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('post-Vid-detail', kwargs={'pk': self.pk})
