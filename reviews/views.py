from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View

# from .models import Review


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


# Instead of the above, we can also use the following, but we'll have to check th request method
# def review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)

#         # This can be used to update an existing review and is possible because of the model form
#         # existing_review = Review.objects.get(id=1)
#         # form = ReviewForm(request.POST, instance=existing_review)

#         if form.is_valid():
#             # review = Review(
#             #     user_name=form.cleaned_data["user_name"],
#             #     review_text=form.cleaned_data["review_text"],
#             #     rating=form.cleaned_data["rating"],
#             # )
#             # review.save()

#             # This is possible because of the model form, we don't need to do this manually
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()
#     return render(request, "reviews/review.html", {"form": form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")
