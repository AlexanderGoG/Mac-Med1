from django.contrib import admin

# Register your models here.
# Define the admin class
from core.models import Problems, Status, Obrashenie


class ProblemsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    ordering = ['name']
    search_fields = ['id','name']
    save_as = True
    save_on_top = True
# Register the admin class with the associated model
admin.site.register(Problems, ProblemsAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    ordering = ['name']
    search_fields = ['id','name']
    save_as = True
    save_on_top = True
# Register the admin class with the associated model
admin.site.register(Status, StatusAdmin)

class ObrashenieAdmin(admin.ModelAdmin):
    list_display = ['id','phone','data_vnesenia','first_name','second_name','otchestvo','vozrast','pol','adress','status','problems']
    ordering = ['data_vnesenia']
    search_fields = ['id',
                     'phone',
                     'first_name',
                     'second_name',
                     'vozrast',
                     'pol',
                     'data_vnesenia',
                     'opisanie',
                     'adress',
                     ]
    list_filter = ['status','problems']
    save_as = True
    save_on_top = True
# Register the admin class with the associated model
admin.site.register(Obrashenie, ObrashenieAdmin)