from django.db import models


# Create your models here.
class Greeting(models.Model):
	when = models.DateTimeField("date created", auto_now_add=True)


class BlogPost(models.Model):
	class Meta:
		ordering = ('-timestamp',)
	
	title = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField()


class URLS(models.Model):
	url = models.CharField(max_length=4096)
	uuid = models.CharField(max_length=64)


class User(models.Model):
	user_name = models.CharField(max_length=128)
	email = models.CharField(max_length=128)
	password = models.CharField(max_length=128)


class UserTags(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=50)


class UserBookmarks(models.Model):
	url = models.ForeignKey(URLS, on_delete=models.CASCADE)
	tags = models.ManyToManyField(UserTags)
	notes = models.TextField(max_length=500)
	date = models.DateTimeField()
