from django.contrib import admin

from .models import (
    Education,
    Experience,
    Leadership,
    Profile,
    Project,
    Skill,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


for model in (Skill, Project, Education, Experience, Leadership):
    admin.site.register(model)
admin.site.site_header = "Muhamad Riki Efendi • CONTENT MANAGER"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Kelola konten portfolio"