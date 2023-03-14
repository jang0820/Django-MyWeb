from django.shortcuts import render
from .models import Todo
from .forms import TodoModelForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

class TodoListView(ListView):
    model = Todo
    queryset = Todo.objects.filter(finish=False)  # 指定查詢條件
    template_name = 'todo/todo_list.html'  # 樣板路徑

    def get_context_data(self, **kwargs):  # 要傳遞的資料
        context = super().get_context_data(**kwargs)
        context["form"] = TodoModelForm()  # 資料模型表單
        return context


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoModelForm  # 使用的表單類別
    success_url = '/todo'  # 儲存成功後要導向的網址


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoModelForm  # 使用的表單類別
    template_name = 'todo/todo_update.html'  # 修改樣板
    success_url = '/todo'  # 儲存成功後要導向的網址


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/todo_delete.html'  # 刪除樣板
    success_url = '/todo'  # 刪除成功後要導向的網址


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/todo_detail.html'
