from django.db import models


class Country(models.Model):
	name = models.CharField(max_length=40)

	def __str__(self):
		return self.name

class Division(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	name = models.CharField(max_length=40)

	def __str__(self):
		return self.name

class District(models.Model):
	division = models.ForeignKey(Division, on_delete=models.CASCADE)
	name = models.CharField(max_length=40)

	def __str__(self):
		return self.name

class SubDistrict(models.Model):
	district = models.ForeignKey(District, on_delete=models.CASCADE)
	name = models.CharField(max_length=40)

	def __str__(self):
		return self.name

class Person(models.Model):
	name = models.CharField(max_length=40)
	father_name = models.CharField(max_length=40)
	mother_name = models.CharField(max_length=40)
	nid = models.CharField(max_length=40)
	religion = models.CharField(max_length=50)
	image = models.FileField(upload_to="person image")
	married_status = models.BooleanField(default=False)

	subdistrict = models.ForeignKey(SubDistrict, on_delete=models.CASCADE)
	district = models.ForeignKey(District, on_delete=models.CASCADE)
	division = models.ForeignKey(Division, on_delete=models.CASCADE)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
    
