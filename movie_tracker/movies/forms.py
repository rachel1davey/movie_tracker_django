from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["body", "rating"]
        widgets = {
            "body": forms.Textarea(attrs={"rows": 3, "placeholder": "Write your review..."}),
            "rating": forms.NumberInput(attrs={"min": 0, "max": 5}),
        }

    def __init__(self, *args, **kwargs):
        # pull the user and movie_id from the view when the form is created
        self.user = kwargs.pop("user", None)
        self.movie_id = kwargs.pop("movie_id", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if self.user and self.movie_id:
            # check if this user already has a review for this movie
            exists = Review.objects.filter(author=self.user, movie_id=self.movie_id).exists()
            if exists:
                raise forms.ValidationError("You’ve already reviewed this movie.")
        return cleaned_data