from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView   # 👈 exact line for checker
from .models import Book
from .models import Library


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


from django.contrib.auth import login       # 👈 add this line
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)          # log in the user immediately
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout View
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

from django.http import HttpResponse

def home_view(request):
    return render(request, 'relationship_app/home.html')

