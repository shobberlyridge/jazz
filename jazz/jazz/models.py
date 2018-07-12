from django.db import models

class People(models.Model):
	sex_choices = (("m", "Male"), ("f", "Female"), ("n", "n/k"))
	
	last_name = models.CharField(max_length=20)
	first_name = models.CharField(max_length=20, blank=True, null=True)
	birth_date = models.DateField(blank=True, null=True)
	sex = models.CharField(max_length=1, choices=sex_choices, default='n')
	main_instrument = models.CharField(max_length=20, blank=True, null=True)
	
	def __unicode__(self):              # __unicode__ on Python 2
		return self.last_name
		
	class Meta:
		verbose_name_plural = 'People'

class Group(models.Model):
	group_name = models.CharField(max_length=30)
	
	def __unicode__(self):              # __unicode__ on Python 2
		return self.group_name
		
	class Meta:
		verbose_name_plural = 'Groups'
		

class Lineup(models.Model):
    group_name = models.ForeignKey(Group, on_delete=models.PROTECT)
    date = models.DateField('Date', blank=True, null=True)
    
    def __unicode__(self):              # __unicode__ on Python 2
        return unicode(self.group_name)
        # return unicode(self.date)
        
    class Meta:
        verbose_name_plural = 'Lineups'
        unique_together = ('group_name', 'date')
