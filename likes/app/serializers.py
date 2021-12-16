from rest_framework import serializers

from .models import Posts

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ('post_id', 'post_name', 'post_description', 'no_of_likes', 'likes', 'hashtags')