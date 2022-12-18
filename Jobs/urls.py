from django.urls import path
from . import views


urlpatterns = [
    path('job-list', views.job_list, name='job-list'),
    path('previous-jobs', views.previous_jobs, name='previous-jobs'),
    path('pending-job-list', views.pending_job_list, name='pending-job-list'),
    path('my-jobs', views.my_jobs, name='my-jobs'),
    path('job-detail/<str:pk>/afripal', views.job_detail, name='job-detail'),
    path('create-job', views.create_job, name='create-job'),
    path('job-update/<str:pk>/afripal', views.job_update, name='job-update'),
    path('job-delete/<str:pk>/afripal', views.job_delete, name='job-delete'),
]