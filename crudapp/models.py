from django.db import models

# Create your models here.
class student(models.Model):
	name=models.CharField(max_length=30)
	rollnum=models.CharField(max_length=30)
	age=models.IntegerField()
	mobile=models.CharField(max_length=30)
	email=models.EmailField(max_length=30)
	address=models.TextField()

	def _str_(self):
		return self.name+' '+self.email