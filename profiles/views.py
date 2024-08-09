from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect


def store_file(file):
    with open("media/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        profile_image = request.FILES["image"]
        store_file(profile_image)
        return HttpResponseRedirect("/profiles")
