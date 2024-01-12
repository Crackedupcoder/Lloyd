from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resume/')
    portfolio = models.CharField(max_length=3000)
    linkedin = models.CharField(max_length=3000)

    def __str__(self):
        return self.name