from django import forms
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio"]
        widgets = {
          "avatar": forms.ClearableFileInput(),
           "bio": forms.Textarea(attrs={"rows": 5, "placeholder": "Edit your bio..."}),
          }


class ProfileSettingsForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ["username"]
    widgets = {
      "username": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
    }