from django.db import models

class Data(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    countryName = models.CharField(max_length=100, null=False, unique=True)
    coronaPositive = models.IntegerField(null=False)
    death = models.IntegerField(null=False)

    def __str__(self):
        return self.countryName
