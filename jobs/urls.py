from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('post/', views.job_post, name='job_post'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
]
