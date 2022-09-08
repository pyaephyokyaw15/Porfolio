from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    banner = models.ImageField(upload_to='images/post_banners/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.id])