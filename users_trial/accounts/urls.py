from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
app_name = 'accounts'

urlpatterns = [
    path('user/<pk>/',views.UserDetail.as_view(),name='userdetail'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name='accounts/user_login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

]
