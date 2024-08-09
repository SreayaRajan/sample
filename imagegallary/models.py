from django.db import models

# Create your models here.
class imagegallary(models.Model):
    caption =models.CharField(max_length=100)
    image=models.ImageField(upload_to="img")

    def _str_(self):
        return self.caption