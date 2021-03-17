from django import forms


class FreeLessonForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 't-input',
                                                           'id': 'some_deewdid',
                                                           'placeholder': 'Электронная почта',
                                                           'style': 'color:#000; border:1px solid #000; '
                                                                    'background-color:#fff; '
                                                                    'border-radius:8px; '
                                                                    '-moz-border-radius:8px; '
                                                                    '-webkit-border-radius:8px;'
                                                                    'font-size:16px;'
                                                                    'font-weight:400;'
                                                                    'height:50px;'}))
