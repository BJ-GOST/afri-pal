from django.urls import path 
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('client-page', views.client_page, name='client-page'),
    path('admin-page', views.admin_page, name='admin-page'),
    path('logout', views.logout, name='logout'),
    path('contacts', views.contact_page, name='contacts')

]
