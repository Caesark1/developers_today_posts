from django.db.models import F, Value
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from apps.posts.models import Post, Comment, Vote


class PostCreateSerializer(serializers.ModelSerializer):
    link = serializers.SlugField(required=False)

    class Meta:
        model = Post
        fields = (
            "title",
            "link",
        )

    def create(self, validated_data):
        post = Post.objects.create(
            **validated_data, author=self.context.get("request").user
        )
        return post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username")
    voted = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "votes_count",
            "voted",
            "author",
        )

    def get_voted(self, data):
        return Vote.objects.filter(
            post=data, user=self.context.get("request").user
        ).exists()


class VoteSerializer(serializers.Serializer):
    votes_count = serializers.BooleanField(default=True)
    posts_id = serializers.IntegerField()

    def validate(self, attrs):
        post = get_object_or_404(Post, id=attrs.get("posts_id"))
        if attrs.get("votes_count"):
            post.votes_count = F("votes_count") + Value(1)
            post.save(update_fields=["votes_count"])
            Vote.objects.create(
                post=post, user=self.context.get("request").user, voted=True
            )
        return attrs


class CommentSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField(required=True)

    class Meta:
        model = Comment
        fields = ("id", "comment_author", "text", "creation_date", "post_id")

    def create(self, validated_data):
        post = get_object_or_404(Post, id=validated_data.pop("post_id"))
        comment = Comment.objects.create(post=post, **validated_data)
        return comment
