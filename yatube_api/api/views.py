from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        """Установка автора при создании поста."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostCommentsViewSet(viewsets.ModelViewSet):
    """Вьюсет для получения комментариев к конкретному посту."""
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        """Возвращаем queryset комментариев для запрошенного поста."""
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return post.comments.all().select_related('author')

    def perform_create(self, serializer):
        """Установка автора и связанного поста при создании комментария."""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
