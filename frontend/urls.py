from django.urls import path 
from .import views

urlpatterns = [
    path('detail-view/<str:pk>/afripal', views.detail_view, name='detail-view'),
    path('mark', views.mark, name='mark')
]