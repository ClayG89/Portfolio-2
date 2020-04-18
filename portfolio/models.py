from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    blog = models.CharField(max_length=1500)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.blogs

class Contact(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField()
    topic = models.CharField(max_length=250)
    message = models.CharField(max_length=400)

    def __str__(self):
        return self.name