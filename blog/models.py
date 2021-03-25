from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    #can be used auto_now_add = True, but it can't be altered
    created_at = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})
    