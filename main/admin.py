from django.contrib import admin

from . models import TeamMembers, Teams, CciGroups,Designations,Billable_Status,Employee_Status,CompanyAssets,Dongle,Mouse,KeyBoard,Laptop,UserAssignedAccessories

admin.site.register(TeamMembers)
admin.site.register(Teams)
admin.site.register(CciGroups)
admin.site.register(Designations)
admin.site.register(Billable_Status)
admin.site.register(Employee_Status)
admin.site.register(CompanyAssets)
admin.site.register(Dongle)
admin.site.register(Mouse)
admin.site.register(KeyBoard)
admin.site.register(Laptop)
admin.site.register(UserAssignedAccessories)
