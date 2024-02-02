from django.contrib import admin
from .models import Profile, Project, ProjectMember, Task

# # Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Task)
