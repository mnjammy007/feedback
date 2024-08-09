from django import forms
from django.db import models
from .models import Review

class ReviewForm(forms.ModelForm):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()

    class Meta:
        model = Review
        fields = "__all__"
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
