from django.db import models

class Hospital(models.Model):
    hospitalName = models.CharField(max_length=200)
    hospitalType = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.hospitalName}({self.hospitalType})"