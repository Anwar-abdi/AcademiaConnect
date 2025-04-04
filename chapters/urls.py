from django.urls import path
from . import views

app_name = 'chapters'

urlpatterns = [
    path('', views.home, name='home'),
    path('chapter/<str:chapter_code>/', views.chapter_detail, name='chapter_detail'),
    path('register/', views.register, name='register'),
    path('registration-status/', views.registration_status, name='registration_status'),
]