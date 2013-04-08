from django.db import models

class ClassA(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class ClassB(models.Model):
	name = models.CharField(max_length=100)
	another_field = models.IntegerField()
	our_class_a = models.ForeignKey(ClassA)

	def __unicode__(self):
		return self.name
