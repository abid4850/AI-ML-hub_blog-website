from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import SimplePost, Category
from .forms import CustomUserCreationForm, PostForm

def home(request):
    try:
        posts = SimplePost.objects.filter(published=True).select_related('author')[:3]
        return render(request, 'home.html', {'posts': posts})
    except Exception:
        messages.error(request, 'Error loading recent posts.')
        return render(request, 'home.html', {'posts': []})


def research(request):
    return render(request, 'research.html')


def projects(request):
    return render(request, 'projects.html')


def blog(request):
    try:
        posts = (
            SimplePost.objects.filter(published=True)
            .select_related('author', 'category')
            .order_by('-created_at')
        )
        categories = Category.objects.all()
        context = {
            'posts': posts,
            'categories': categories
        }
        return render(request, 'blog.html', context)
    except Exception:
        messages.error(request, 'An error occurred while loading the blog posts.')
        return render(request, 'blog.html', {'posts': [], 'categories': []})


def datasets(request):
    return render(request, 'datasets.html')


def tools(request):  # Single view for /tools/
    return render(request, 'tools.html')


def features(request):
    return render(request, 'features.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})
