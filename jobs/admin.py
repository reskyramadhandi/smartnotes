from django.contrib import admin
from .models import Job

# Register your models here.


class JobsAdmin(admin.ModelAdmin):
    list_display = ('summary',)


admin.site.register(Job, JobsAdmin)
