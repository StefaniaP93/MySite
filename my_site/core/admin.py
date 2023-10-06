from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'image',
        'carousel',
    ]
    readonly_fields = ['slug']

admin.site.register(Project, ProjectAdmin)
