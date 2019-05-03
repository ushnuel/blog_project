from django.urls import reverse
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE) #only allow the authorized user to perform CRUD
    title = models.CharField(max_length=256)
    text = models.TextField()
    date_create = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def publish_post(self):
        self.date_published = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete= models.CASCADE, related_name='comments')
    author = models.CharField(max_length=256)
    text = models.TextField()
    date_create = models.DateTimeField(default=timezone.now)
    approved_comments = models.BooleanField(default=False)
    date_published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.text

    def approve(self):
        self.approved_comments = True
        self.save()

    #redirect to post_list url after creating comments
    def get_absolute_url(self):
        return reverse('post_list')
