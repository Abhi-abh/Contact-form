from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)  
    pdf = models.FileField(upload_to='media/pdfs/', blank=True, null=True) 

    def __str__(self):
        return self.name
