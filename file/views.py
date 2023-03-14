from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.utils.http import urlquote
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import models
import os

@login_required
def uploadFile(request):
    if request.method == "POST":
        if request.POST["fileTitle"]:
            fileTitle = request.POST["fileTitle"]
        else:
            fileTitle = request.FILES["uploadedFile"].name
        if request.user.is_authenticated and request.user.has_perm('file.file_upload'):
            uploadedFile = request.FILES["uploadedFile"]
            file = models.File(
            	title = fileTitle,
            	uploadedFile = uploadedFile,
            	user = request.user
            )
            file.save()
    files = models.File.objects.all()
    return render(request, "upload-file.html", context = { "files": files })


@login_required
def deleteFile(request, pk):
    dir = 'media/'
    deletefile = models.File.objects.filter(pk = pk)
    f = deletefile[0]
    if (f.user == request.user and request.user.has_perm('file.file_delete')): #檔案上傳者且有刪除權限者才能刪除
        os.remove(dir+'{}'.format(f.uploadedFile))
        models.File.objects.filter(pk = pk).delete()
    return HttpResponseRedirect(reverse('file:upload'))


@login_required
def downloadFile(request, pk):
    file = models.File.objects.filter(pk=pk)
    dir = 'media/'
    if file:
        f = file[0]
        path = dir+'{}'.format(f.uploadedFile)
        file = open(path, 'rb') # 讀取檔案
        response = FileResponse(file)
        di,fi = str(f.uploadedFile).split('/') #資料夾與檔名分開
        response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(fi)  #urlquote對檔名稱進行編碼
        return response
    else:
        return HttpResponse('檔案不存在!')
