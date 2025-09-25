from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio"]
        widgets = {
          "avatar": forms.ClearableFileInput(),
           "bio": forms.Textarea(attrs={"rows": 5, "placeholder": "Edit your bio..."}),
          }