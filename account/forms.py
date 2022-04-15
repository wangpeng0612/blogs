from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(label="账号", widget=forms.TextInput(
        attrs={'class': "form-control", 'required': "", 'placeholder': '输入账号'}))
    password = forms.CharField(widget=forms.PasswordInput, label='密码')


class AuthenticationForm1(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': "form-control", 'required': "", 'placeholder': '输入账号'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': "form-control", 'required': "", 'placeholder': '输入密码'}),
    )


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='账号', widget=forms.TextInput(
        attrs={'class': "form-control", 'required': "", 'placeholder': '请输入账号'}))
    email = forms.EmailField(label='邮箱', widget=forms.EmailInput(
        attrs={'class': "form-control", 'required': "", 'placeholder': '请输入邮箱'}))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(
        attrs={'class': "form-control", 'required': "", 'placeholder': '输入密码'}))
    password2 = forms.CharField(label="确认密码", widget=forms.PasswordInput(
        attrs={'class': "form-control", 'required': "", 'placeholder': '确认密码'}))

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("两次密码不一致")
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    nickname = forms.CharField(label='用户名', widget=forms.TextInput(
        attrs={'class': "form-control", 'required': "", 'placeholder': '请输入用户名'}))

    class Meta:
        model = UserProfile
        fields = ('nickname',)
