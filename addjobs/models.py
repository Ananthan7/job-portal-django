from django.db import models


# Create your models here.
class Jobs(models.Model):
    post = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    lastdate = models.CharField(max_length=50)

    # pdf = models.FileField(upload_to='book/pdf')


    def __str__(self):
        return self.title