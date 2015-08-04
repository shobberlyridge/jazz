from django.contrib import admin
from jazz.models import People, Group

class PeopleAdmin(admin.ModelAdmin):
	list_display = ['last_name', 'first_name', 'sex', 'birth_date', 'main_instrument']

class GroupAdmin(admin.ModelAdmin):
	list_display = ['group_name']

admin.site.register(People, PeopleAdmin)
admin.site.register(Group, GroupAdmin)
