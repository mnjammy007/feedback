from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Review


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {"form": form})


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self) -> QuerySet[Any]:
    #     base_query = super().get_queryset()
    #     new_query = base_query.filter(rating__gte=3)
    #     return new_query


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["pk"]
    #     review = Review.objects.get(pk=review_id)
    #     context["review"] = review
    #     return context
