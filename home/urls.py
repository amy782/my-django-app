from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index , name= 'home'),
    path('signup/', views.user_signup , name= 'signup'),
    path('login/', views.user_login , name= 'login'),
    path('logout/', views.user_logout , name= 'logout'),
    path('create_post', views.create_post , name= 'create_post'),
    path('all_posts', views.all_posts , name= 'all_posts'),
    path('my_posts', views.my_posts , name= 'my_posts'),
    path('dlt/<int:pk>', views.dlt , name= 'dlt'),
    path('edit/<int:pk>', views.edit , name= 'edit'),
    path('profile', views.view_profile , name= 'profile'),
    path('edit_profile', views.edit_profile , name= 'edit_profile'),
]