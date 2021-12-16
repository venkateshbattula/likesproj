from django.db import models

# Create your models here.
class Posts(models.Model):
    post_id = models.AutoField.unique
    post_name = models.CharField(max_length=60)
    post_description = models.CharField(max_length=60)
    attached_files = models.FileField()
    no_of_likes = models.IntegerField(default=0)
    hashtags = models.CharField(max_length=250)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_name

    def postLikes(self, post_id):
        user_id = models.IntegerField(unique=True)
        post_id = models.IntegerField(unique=True)
        time = models.DateTimeField(auto_now=True)
        return post_id, user_id
