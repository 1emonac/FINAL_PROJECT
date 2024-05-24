from django import forms
from users.models import User
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '아이디', 'required': True, 'autofocus': True},
        )
    )
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': '비밀번호', 'required': True},
        )    
    )

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '아이디', 'class': 'form-control', 'required': True, 'autofocus': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': '이메일', 'class': 'form-control', 'required': True, 'autofocus': True}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 (4자리 이상)', 'class': 'form-control', 'required': True, 'autofocus': True}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 확인 (4자리 이상)', 'class': 'form-control', 'required': True, 'autofocus': True}))

    def clean_username(self):
        username = self.cleaned_data["username"]

        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 아이디({username})은 이미 사용 중입니다")
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise ValidationError(f"입력한 이메일({email})은 이미 사용 중입니다")
        
        return email
    
    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            # password2 필드에 오류를 추가
            self.add_error("password2",
                           "비밀번호와 비밀번호 확인란의 값이 다릅니다")
            
    def save(self):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password1 = self.cleaned_data["password1"]

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,

        )
        return user