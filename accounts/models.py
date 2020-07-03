from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField


class Profile(models.Model):
    user = AutoOneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    inpost_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} {self.inpost_code}"
