from django.contrib import admin
from jazz.models import People, Group, Lineup

class PeopleAdmin(admin.ModelAdmin):
	list_display = ['last_name', 'first_name', 'sex', 'birth_date', 'main_instrument']

class GroupAdmin(admin.ModelAdmin):
	list_display = ['group_name']
	
class LineupAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'date']

admin.site.register(People, PeopleAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Lineup, LineupAdmin)
