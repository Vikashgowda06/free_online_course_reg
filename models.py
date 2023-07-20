from django.db import models

class registration(models.Model):
    name = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=20)
    email = models.EmailField()
    internshipprogram=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.name



