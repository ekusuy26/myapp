from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import UserInfo

User = get_user_model()

class RegistForm(UserCreationForm):
    image = forms.ImageField()
    error_message = ''
    username = forms.CharField(label='LOGIN_ID', max_length=30,
        widget=forms.TextInput(
        attrs={'placeholder':'名前を入力してください', 'class':'form-control'}))
    email = forms.CharField(label='EMAIL', max_length=30,
        widget=forms.TextInput(
        attrs={'placeholder':'emailを入力してください', 'class':'form-control', 'autocomplete': 'email'}))
    password1 = forms.CharField(
        label='PASSWORD', max_length=128,
        widget=forms.PasswordInput(
        attrs={'placeholder':'パスワードを入力してください', 'class':'form-control', 'autocomplete' : 'off'}))
    password2 = forms.CharField(
        label='PASSWORDCONFIRM', max_length=128,
        widget=forms.PasswordInput(
        attrs={'placeholder':'パスワードを再度入力してください', 'class':'form-control', 'autocomplete' : 'off'}))
    self_introduction = forms.CharField(required=False, label='SELF_INTRODUCTION', max_length=1000,
        widget=forms.Textarea(
        attrs={'rows' : 10, 'class':'form-control'}))
    is_save = False
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, post):
        user = super().save()
        info = UserInfo()
        info.origin = self.cleaned_data['image']
        info.id = user.id
        info.user_id = user.id
        info.name = post['username']
        info.self_introduction = post['self_introduction']
        info.save()
        
        self.is_save = True

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる