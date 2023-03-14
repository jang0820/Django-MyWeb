from django.contrib import admin
from .models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploadedFile', 'dateTimeOfUpload', 'user')

admin.site.register(File, FileAdmin)
