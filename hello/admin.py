from django.contrib import admin

# Register your models here.
from hello.models import *


class GreetingAdmin(admin.ModelAdmin):
	# ~ fields = ('when',)
	pass


class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp')


class UserBookmarksAdmin(admin.ModelAdmin):
	pass


class UserTagsAdmin(admin.ModelAdmin):
	pass


class URLSAdmin(admin.ModelAdmin):
	pass


class UserAdmin(admin.ModelAdmin):
	pass


admin.site.register(Greeting, GreetingAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(UserBookmarks, UserBookmarksAdmin)
admin.site.register(UserTags, UserTagsAdmin)
admin.site.register(URLS, URLSAdmin)
admin.site.register(User, UserAdmin)
# admin.site.register(BlogPost, BlogPostAdmin)
