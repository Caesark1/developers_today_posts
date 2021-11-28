from django.contrib import admin

from apps.posts.models import Post, Comment, Vote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'author')
    search_fields = ('title',)
    list_filter = ('title', 'author')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', )


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
