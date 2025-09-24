from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('research/', views.research, name='research'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog, name='blog'),
    path('datasets/', views.datasets, name='datasets'),
    path('tools/', views.tools, name='tools'),
    path('about-contact/', views.about_contact, name='about_contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
