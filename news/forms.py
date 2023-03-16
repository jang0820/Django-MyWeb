from django import forms
from .models import News

class NewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content','file1','file2','file3')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '標題'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '內容'}),
            'file1': forms.FileInput(attrs={'class': 'form-control', 'placeholder': '上傳附件1'}),
            'file2': forms.FileInput(attrs={'class': 'form-control', 'placeholder': '上傳附件2'}),
            'file3': forms.FileInput(attrs={'class': 'form-control', 'placeholder': '上傳附件3'}),
        }