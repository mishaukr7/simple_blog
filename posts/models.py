from django.db import models
from accounts.models import Profile, User
from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='upload', default='upload/default.jpg')

    def get_absolute_url(self):

        return reverse('posts:post', args=[str(self.id)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    path = ArrayField(models.IntegerField())
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='post_comments')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_comments')
    content = models.TextField('Comment', max_length=1024)
    pub_date = models.DateTimeField('Time create', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def get_offset(self):
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return level

    def get_col(self):
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return 12 - level

    def __str__(self):
        return self.content[0:200]

