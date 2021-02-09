from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # поля для заполнения
        fields = ('name', 'text')
        # псевдонимы полей для заполнения
        labels = {'name': 'Представьтесь',
                  'text': 'Ваш комментарий',
                  }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'back_form'})
        self.fields['text'].widget.attrs.update({'class': 'back_form'})

