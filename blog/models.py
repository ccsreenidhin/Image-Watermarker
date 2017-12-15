from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User




class Document(models.Model):
    user = models.ForeignKey(User) 
    orimage = models.ImageField(upload_to='original', null = True)
    dupimage = models.ImageField(upload_to='wmarked', null = True)
    text = models.CharField(max_length =200, null = True)
    x = models.IntegerField(null = True)
    y = models.IntegerField(null = True)
    color = models.CharField(max_length =200, null = True)
    fontsize = models.CharField(max_length =200, null = True)




  
