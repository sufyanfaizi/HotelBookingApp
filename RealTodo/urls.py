from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.index , name='index'),
    path('Tasks/', views.tasks , name='tasks'),
    path('Tasks/<int:pk>/', views.tasksall , name='tasksall'),
    path('Home/', views.Home , name='Home'),
    path('Home/<int:pk>/', views.tasksall , name='tasksall'),
    #path('hotel_booking/', views.hotel_booking , name='hotel_booking'),
    #path('hotel_booking/home/<int:pk>/', views.booking_details , name='booking_details'),
    #path('hotel_booking/home/', views.home , name='home'),
    path('hotel_booking/AboutUs/', views.AboutUs , name='AboutUs'),
    path('hotel_booking/Details/', views.Details , name='Details'),
    path('hotel_booking/Details/<int:pk>/', views.booking_details , name='booking_details'),
    path('hotel_booking/Pricing/', views.Pricing , name='Pricing'),
    path('', views.home , name='home'),


]

