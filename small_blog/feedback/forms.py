from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('text', 'author', 'email')
        widgets = {
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'class': 'form-control input-lg emailAddress',
                'name': 'email',
                'placeholder': 'email'}),
            'text': forms.Textarea(attrs={
                'rows':8,
                'placeholder': 'Текст...'}),
            'author': forms.TextInput(attrs={
                'placeholder': 'ФИО'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "... и действующий адрес электронной почты:"
        self.fields['text'].label = "Текст отзыва"
        self.fields['author'].label = "Укажите Ваши фамилию, имя и отчество (при наличии):"
