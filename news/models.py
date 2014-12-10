from django.db import models

# Create your models here.
class NewsPost(models.Model):
	title = models.CharField(max_length=50)
	