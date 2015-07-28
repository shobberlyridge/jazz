from django.db import models

class People(models.Model):
    last_name = models.CharField(max_length=20) 
    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.last_name
