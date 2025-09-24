from django.urls import path
from main import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('blog/', views.blog, name='blog'),
    path('projects/', views.projects, name='projects'),
    path('research/', views.research, name='research'),
    path('datasets/', views.datasets, name='datasets'),
    path('tools/', views.tools, name='tools'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
