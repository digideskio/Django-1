from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length = 120)
	content = models.TextField(blank = True)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
	update = models.DateTimeField(auto_now = True, auto_now_add = False)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

class Hapus(models.Model):
	delete = models.ForeignKey(Post, on_delete = models.CASCADE)