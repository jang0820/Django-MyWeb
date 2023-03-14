from django.db import models
from django.conf import settings

class File(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "UploadedFile/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='file_user', null = True)
    class Meta:
        permissions = (
            ("file_upload", "Can Upload File"),
            ("file_delete", "Can Delete File"),
        )