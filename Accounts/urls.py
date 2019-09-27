from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    #path('login/', LoginView.as_view(), name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
   

]
