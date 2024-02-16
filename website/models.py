from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250, blank=True, null=True)
    message = models.TextField()
    creaded_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['creaded_date']
        
    
    
class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

# Create your models here.
