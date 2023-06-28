from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),

]