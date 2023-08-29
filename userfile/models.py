from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserLogin(AbstractUser):
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    

class UserCsvFile(models.Model):
    name = models.ForeignKey(UserLogin,on_delete=models.CASCADE)
    csv_file = models.FileField(upload_to='csv_files/')

    def __str__(self):
        return self.name.username
    
class CSVModel(models.Model):
    shop1 = models.CharField(max_length=100)
    shop2 = models.CharField(max_length=100)
    total_inventary = models.IntegerField()
    minimum_stock = models.IntegerField()

    def __str__(self):
        return self.shop1

    

