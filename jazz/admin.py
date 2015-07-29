from django.contrib import admin
from jazz.models import People

class PeopleAdmin(admin.ModelAdmin):
	list_display = ['last_name', 'first_name', 'birth_date']

admin.site.register(People, PeopleAdmin)
