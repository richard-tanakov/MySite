from .models import Articles
from django.forms import ModelForm, Textarea, DateTimeInput, TextInput

class ArticlesForm (ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons','full_text','data']
        
        widgets= {
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder':"Название статьи"
            }),
            'anons': TextInput(attrs={
                'class':'form-control',
                'placeholder':"Анонс статьи"
            }),
            'data': DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':"Дата и время"
    
            }),
    
            'full_text': Textarea(attrs={
                'class':'form-control',
                'placeholder':"Текст статьи"
    
            })
            
        }