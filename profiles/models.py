from django.db import models


class UserProfile(models.Model):
    user_image = models.ImageField(upload_to="images")