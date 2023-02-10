from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import LimitOffsetPagination

from .mixins import CreateListViewSet
from .permissions import IsAuthorOrReadOnly
from .serializers import (PostSerializer, GroupSerializer, CommentSerializer,
                          FollowSerializer)

from posts.models import Post, Group


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Показывает список групп"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowViewSet(CreateListViewSet):
    """Список подписок. Создание подписок"""

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('$following__username',)

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    """Список постов. Редактирование постов"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Список коментариев. Редактирование коментариев"""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        new_queryset = get_object_or_404(Post, id=post_id)
        return new_queryset.comments
