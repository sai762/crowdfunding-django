from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index,name="index"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('register/',views.registerUser, name='register'),
    path("fund_project/<int:pId>", views.fund_project,name="fund_project"),
    path("all-projects/",views.list_projects,name="all_projects"),
    path("all-projects/<int:pId>",views.view_project, name="view_project"),
    path("add-project/", views.add_project,name="add_project"),
    path("all-projects/<str:ptype>", views.project_type, name="project_type"),
    # path('accounts/register/', register, name='register'),
    # path('accounts/profile',views.profile, name='profile'),
    
     
    
]