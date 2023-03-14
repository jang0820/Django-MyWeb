from django import forms
from .models import Todo

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'finish')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '待辦事項'})
        }
