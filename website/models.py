from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    creaded_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['creaded_date']
        
    def __str__(self):
        return self.subject
    
class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

# Create your models here.
