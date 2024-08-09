from django.urls import path
from . import views

urlpatterns = [
    # path("", views.review, name="review-form"),
    path("", views.ReviewView.as_view(), name="review-form"),
    path("thank-you/", views.thank_you, name="thank-you"),
]
