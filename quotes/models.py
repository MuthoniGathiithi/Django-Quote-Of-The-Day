from django.db import models
class Quote(models.Model):
    quote_text=models.CharField(max_length=255)
    author=models.CharField(max_length=100)

# Create your models here.
