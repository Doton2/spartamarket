from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms



# class CustomUserCreationForm(forms.Form):
#     username=forms.CharField(help_text="내용을 추가")



# class CustomUserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].help_text = ""
#         self.fields['password1'].help_text = ""
    # class Meta(UserCreationForm.Meta):
    #     model = get_user_model()
    #     fields = [
    #         'username', 'email','password1','password2'
    #     ]
        
        