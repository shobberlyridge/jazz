from django.db import models

class People(models.Model):
    last_name = models.CharField(max_length=20)   
    first_name = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.last_name
        
    class Meta:
        verbose_name_plural = 'People'
