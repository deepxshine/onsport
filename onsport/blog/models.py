from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL,
                                 null=True, related_name='category')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author')
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, default='Название')

    def __str__(self):
        return self.text[:30]

    class Meta:
        ordering = ['pub_date']


class Comment:
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='post_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='author_comment')
    text = models.CharField(max_length=5000)

    def __str__(self):
        return self.text[:30]
