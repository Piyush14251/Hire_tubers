from django.contrib import admin
from .models import Youtubers
from django.utils.html import format_html
# Register your models here.
class ytAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))

    list_display = ('id', 'name', 'myphoto', 'sub_count', 'is_featured')
    search_fields = ('name', 'camera_type')
    list_filter = ('camera_type', 'city')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured',)



admin.site.register(Youtubers, ytAdmin)