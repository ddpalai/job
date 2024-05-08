from django.contrib import admin
from testapp.models import HydJob,BngJob,PunJob

# Register your models here.
class Hydadmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email']
admin.site.register(HydJob,Hydadmin)

class Bngadmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email']
admin.site.register(BngJob,Bngadmin)

class Punadmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email']
admin.site.register(PunJob,Punadmin)