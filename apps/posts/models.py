from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        verbose_name="Title", max_length=255, unique=True
    )
    link = models.SlugField(verbose_name="Link for post")
    creation_date = models.DateTimeField(auto_now_add=True)
    votes_count = models.PositiveIntegerField(verbose_name="Vote counts", default=0)
    author = models.ForeignKey(
        User,
        verbose_name="User that has created this post",
        on_delete=models.CASCADE,
        related_name="posts",
    )

    class Meta:
        ordering = ("votes_count",)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.link:
            self.link = self.title
        super(Post, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title


class Vote(models.Model):
    post = models.ForeignKey(
        Post, verbose_name='Post', on_delete=models.CASCADE,
        related_name='votes'
    )
    user = models.ForeignKey(
        User, verbose_name='User', on_delete=models.CASCADE,
        related_name='votes'
    )
    voted = models.BooleanField(verbose_name='Voted', default=True)

    def __str__(self):
        return f'{self.user.username} voted for {self.post.title}\'s post'


class Comment(models.Model):
    post = models.ForeignKey(
        Post, verbose_name='Posts', on_delete=models.CASCADE,
        related_name='comments'
    )
    comment_author = models.CharField(verbose_name='Author of comment', max_length=100)
    text = models.TextField(verbose_name='Comments\' text')
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-creation_date', )

    def __str__(self):
        return f'Comment on {self.post.title}\'s post. Commented {self.comment_author}'
