from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('news title'))
    content = models.CharField(max_length=10000, verbose_name=_('news content'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='news_user', null = True)
    numclick = models.IntegerField(default=0)
    file1 = models.FileField(upload_to = "newsfile/", null=True, blank=True)  #blank表示轉成表單可以不輸入資料
    file2 = models.FileField(upload_to = "newsfile/", null=True, blank=True)  #blank表示轉成表單可以不輸入資料
    file3 = models.FileField(upload_to = "newsfile/", null=True, blank=True)  #blank表示轉成表單可以不輸入資料
    created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        permissions = (
            ("news_delete", "Can Delete News"),
            ("news_create", "Can Create News"),
            ("news_update", "Can Update News"),
        )