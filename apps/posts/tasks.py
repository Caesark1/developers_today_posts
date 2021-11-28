from huey import crontab
from huey.contrib.djhuey import periodic_task

from apps.posts.models import Post, Vote


@periodic_task(crontab(day='*/1', hour='21'))
def delete_posts_upvotes():
    Vote.objects.all().delete()
    Post.objects.all().update(votes_count=0)
