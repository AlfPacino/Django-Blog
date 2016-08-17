
from django.db import models
from django.utils import timezone
import os

# Create your models here.

def content_file_name(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.author, filename)

_PATH = os.path.abspath(os.path.dirname(__file__))

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Posts_Images', blank=True, null=True)
    text = models.TextField()
    files = models.FileField(upload_to='Files', blank=True, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def attached_file_name(self):
        return os.path.basename(self.files.name)

    def __str__(self):
        return self.title