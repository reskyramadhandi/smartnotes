from django.urls import path

from . import views

urlpatterns = [
    path('', views.JobsView, name='jobs'),
    path('<int:job_id>', views.JobsDetailView, name='jobsdetail'),
]
