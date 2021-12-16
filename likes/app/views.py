from rest_framework import viewsets

from .serializers import PostSerializer
from .models import Posts


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('post_id')
    serializer_class = PostSerializer