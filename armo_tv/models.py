from django.db import models
from django.contrib.auth.models import User

class armo_tv(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    video = models.FileField(default=None,blank=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    extension = models.CharField(max_length=5)
    cover = models.ImageField()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + ' ...'

class Comment(models.Model):
    post = models.ForeignKey(armo_tv ,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
                                
    
