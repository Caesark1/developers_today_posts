from rest_framework import viewsets, generics, status
from rest_framework import permissions
from rest_framework.response import Response

from apps.posts.serializers import (
    PostSerializer,
    PostCreateSerializer,
    VoteSerializer,
    CommentSerializer,
)
from apps.posts.models import Post, Comment, Vote
from apps.posts import permissions as custom_permissions


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.select_related("author").all()
    permission_classes = (
        permissions.IsAuthenticated,
        custom_permissions.IsOwnerOrReadOnly,
    )
    serializer_classes = {
        "list": PostSerializer,
        "create": PostCreateSerializer,
        "retrieve": PostSerializer,
        "delete": PostSerializer,
        "partial_update": PostCreateSerializer,
        "update": PostCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class CommentCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        custom_permissions.IsOwnerOrReadOnly,
    )


class SetVoteAPIView(generics.GenericAPIView):
    serializer_class = VoteSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Vote.objects.all()

    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serialized_data.is_valid(raise_exception=True)
        return Response(
            {"message": "You have successfully voted."},
            status=status.HTTP_204_NO_CONTENT,
        )
