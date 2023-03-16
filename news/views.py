from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.utils.http import urlquote
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, FileResponse, Http404
from django.urls import reverse
import os
from .models import News
from .forms import NewsModelForm

class NewsListView(ListView):
    model = News
    queryset = News.objects.all()  # 指定查詢條件
    template_name = 'news/news_list.html'  # 樣板路徑


class NewsCreateView(CreateView):
    model = News #指定資料表
    form_class = NewsModelForm  # 使用的表單類別
    template_name = 'news/news_create.html'  # 樣板路徑
    success_url = '/news'  # 儲存成功後要導向的網址
    def form_valid(self, form): #寫入資料庫並重導到指定的頁面
        form.instance.user = self.request.user  #News資料表內的user來自於self.request.user
        return super().form_valid(form)
    @method_decorator(login_required)  #需要登入才能使用，修飾dispatch
    def dispatch(self, request, *arg, **kwargs):
        if (request.user.has_perm('news.news_create')): #需要權限news.news_create
            return super().dispatch(request, *arg, **kwargs)
        else:
            raise Http404()


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = News
    form_class = NewsModelForm  # 使用的表單類別
    template_name = 'news/news_update.html'  # 修改樣板
    success_url = '/news'  # 儲存成功後要導向的網址
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        updatenews = News.objects.filter(pk = self.kwargs.get("pk"))  #updatenews為QuerySet物件，每個元素都是News
        context['news'] = updatenews[0]   #增加變數到context
        return context
    def get(self, request, *args, **kwargs):
        news = News.objects.filter(pk = self.kwargs.get("pk"))
        if (news[0].user == request.user and request.user.has_perm('news.news_update')):
            return super().get(request, *args, **kwargs)
        else:
            raise Http404()


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = News
    template_name = 'news/news_delete.html'  # 刪除樣板
    success_url = '/news'  # 刪除成功後要導向的網址，使用/開始表示網頁的根目錄開始

    def form_valid(self, form): #DeleteView的form，呼叫post函式，接著呼叫form_valid後刪除元素
        deletefile = News.objects.filter(pk=self.kwargs.get("pk"))
        f = deletefile[0]
        if (f.user == self.request.user and self.request.user.has_perm('news.news_delete')):  # 檔案上傳者且有刪除權限者才能刪除
            if (f.file1 != ""):
                os.remove('media/' + '{}'.format(f.file1))  # 刪除檔案
            if (f.file2 != ""):
                os.remove('media/' + '{}'.format(f.file2))  # 刪除檔案
            if (f.file3 != ""):
                os.remove('media/' + '{}'.format(f.file3))  # 刪除檔案
        else:
            raise Http404()
        return super(NewsDeleteView, self).form_valid(form)


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'

    def get(self, request, *arg, **kwargs):
        item = News.objects.get(pk = self.kwargs.get("pk"))  #GET網頁時，更新點擊次數
        item.numclick = item.numclick+1
        item.save()
        return super().get(request, *arg, **kwargs)

    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def downloadFile(request, pk, num):
    file = News.objects.filter(pk=pk)
    dir = 'media/'
    if file:
        f = file[0]
        if num == 1:
            path = dir+'{}'.format(f.file1)
        if num == 2:
            path = dir+'{}'.format(f.file2)
        if num == 3:
            path = dir+'{}'.format(f.file3)
        file = open(path, 'rb') # 讀取檔案
        response = FileResponse(file)
        di1, di2, fi = str(path).split('/') #資料夾與檔名分開
        response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(fi)  #urlquote對檔名稱進行編碼
        return response
    else:
        return HttpResponse('檔案不存在!')
