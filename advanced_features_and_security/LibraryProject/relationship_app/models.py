from django.db import models
from django.conf import settings  # <-- use this for custom user
from django.db.models.signals import post_save
from django.dispatch import receiver

# UserProfile model
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # <-- updated to custom user
        on_delete=models.CASCADE
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Signal to automatically create UserProfile for new users
@receiver(post_save, sender=settings.AUTH_USER_MODEL)  # <-- also update sender
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Library model
class Library(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


# Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    copies_available = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
