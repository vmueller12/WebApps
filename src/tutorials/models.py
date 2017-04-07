from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Tutorial(models.Model):
	title = models.CharField(max_length=120) #max_length = 120
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

	# Hardcoded Version of get_absolute_url
	# def get_absolute_url(self):
	# 	return "/tutorials/%s/" %(self.id)

	def get_absolute_url(self):
		return reverse("detail", kwargs={"id": self.id})
	
