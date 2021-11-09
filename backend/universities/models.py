from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    year_founded = models.IntegerField()

    def __str__(self):
        return self.name


class Degree(models.Model):
    name = models.CharField(max_length=255)
    universities = models.ManyToManyField(University)


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    degrees = models.ManyToManyField(Degree)
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class Tags(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE)