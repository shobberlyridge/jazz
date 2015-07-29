from django.contrib import admin
from jazz.models import People

class PeopleAdmin(admin.ModelAdmin):
	fields = ['first_name', 'last_name']

admin.site.register(People, PeopleAdmin)
