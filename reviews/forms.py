from django import forms
from django.db import models
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         label="Your Name",
#         max_length=100,
#         error_messages={
#             "required": "Your name must not be empty!",
#             "max_length": "Please enter a shorter name!",
#         },
#     )
#     review_text = forms.CharField(
#         label="Your Feedback",
#         widget=forms.Textarea,
#         max_length=200,
#     )
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

#     class Meta:
#         fields = ["title", "body", "rating"]


class ReviewForm(forms.ModelForm):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()

    class Meta:
        model = Review
        fields = "__all__"
        # fields = ["user_name", "review_text", "rating"]
        # exclude = ["owner_comment"]
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating",
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!",
            }
        }
