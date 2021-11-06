from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    role = models.CharField(max_length=225)
    fb_link = models.CharField(max_length=225)
    insta_link = models.CharField(max_length=225)
   
    photo = models.ImageField(upload_to='media/team/%y/%d') 
    creat_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Slider(models.Model):
    headline = models.CharField(max_length=225)
    subtitel =models.CharField(max_length=225)
    button_text = models.CharField(max_length=225)
    photo =models.ImageField(upload_to='media/slider/%y/')
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.headline