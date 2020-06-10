from django import forms
class Mail(forms.Form):
    subject=forms.CharField(max_length=10,label='主题')
    message=forms.CharField(max_length=1000,min_length=4,label='信息内容')
    email=forms.EmailField(label='邮箱地址')