from django.db import models

# Create your models here.
class Stock(models.Model):
	ticker = models.CharField(max_length=10)          #charfield is database data type


	def __str__(self):
		return self.ticker                            #this is for our django admin area