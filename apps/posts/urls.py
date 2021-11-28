from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.posts.views import PostViewSet, SetVoteAPIView, CommentCreateAPIView

router = DefaultRouter()

router.register('', PostViewSet, basename='posts')

urlpatterns = [
    path('vote/', SetVoteAPIView.as_view(), name='vote'),
    path('comment/', CommentCreateAPIView.as_view(), name='comments')
]

urlpatterns += router.urls
