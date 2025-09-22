from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # avoid clash with auth.User.groups
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # avoid clash with auth.User.user_permissions
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username

# ----------------------
# Book model for ALX checker
# ----------------------
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.title
