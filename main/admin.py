from django.contrib import admin

from . models import TeamMembers, Teams, CciGroups,Designations,Billable_Status,Employee_Status

admin.site.register(TeamMembers)
admin.site.register(Teams)
admin.site.register(CciGroups)
admin.site.register(Designations)
admin.site.register(Billable_Status)
admin.site.register(Employee_Status)

