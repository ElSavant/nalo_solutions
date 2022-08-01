from django.db import models

# Create your models here.
class Contact(models.Model):

    image = models.ImageField(upload_to='contacts/%Y',blank=True,default="")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100,blank=True,default="")
    phone = models.CharField(max_length=13,unique=True)
    company = models.CharField(max_length=100, blank=True, default='')
    job_title = models.CharField(max_length=100, blank=True, default='')
    birthday = models.DateField(blank=True, default="1900-01-01")
    email = models.EmailField(blank=True,default="")
    date_created = models.DateTimeField(auto_now_add=True)
    


    class Meta:
        ordering = ["date_created","phone"]
        verbose_name_plural = "Contacts"