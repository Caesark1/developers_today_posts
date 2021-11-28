from huey import crontab
from huey.contrib.djhuey import periodic_task

from apps.posts.models import Post, Vote


@periodic_task(crontab(minute='*/1'))
def delete_posts_upvotes():
    Vote.objects.all().delete()
    Post.objects.all().update(votes_count=0)
