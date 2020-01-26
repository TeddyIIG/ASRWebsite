from django.db import models


class UsersLogin(models.Model):
    username = models.CharField(max_length=256, unique=True, primary_key=True)
