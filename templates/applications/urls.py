from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_for_job, name='apply'),
    path('my/', views.my_applications, name='my_applications'),
    path('<int:pk>/', views.application_detail, name='application_detail'),
]
