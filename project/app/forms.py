from django import forms


class Userform(forms.Form):
    name = forms.CharField(required=False,label='Ваше имя:', help_text='sdfewwe',
                             widget=forms.TextInput(attrs={'class': 'myClass'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'myClass'}))
    password = forms.CharField(min_length=8, max_length=10, label = 'Password', widget=forms.PasswordInput)


class AddPost(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
