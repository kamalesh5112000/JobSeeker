from django.contrib import admin

from app.models import Auther, JobPost, Location
class JobAdmin(admin.ModelAdmin):
    list_display=('title','salary','date')
# Register your models here.
admin.site.register(Auther)
admin.site.register(Location)
admin.site.register(JobPost, JobAdmin)