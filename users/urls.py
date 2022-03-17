from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, ChangePasswordView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('all_users', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('reset_password', ChangePasswordView.as_view()),
]
