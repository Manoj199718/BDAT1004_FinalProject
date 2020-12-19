from django.db import models

# Create your models here.

class Flipkart(models.Model):
	name = models.CharField(max_length = 100)
	price = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Amazon(models.Model):
	name = models.CharField(max_length = 100)
	price = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Paytm(models.Model):
	name = models.CharField(max_length = 100)
	price = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Snapdeal(models.Model):
	name = models.CharField(max_length = 100)
	price = models.CharField(max_length = 100)

	def __str__(self):
		return self.name


