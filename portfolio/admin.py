from django.contrib import admin
from .models import Project, Profile


admin.site.site_header = "Portfolio Administration"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to the Portfolio Admin"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "get_links", "position") 
    list_editable = ("position",)

    def get_links(self, obj):
        return ", ".join(obj.links or []) 
    get_links.short_description = 'Links'  

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "github", "linkedin")

