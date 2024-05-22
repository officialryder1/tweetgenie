from django.urls import path
from .views import register_user, check_username, check_email, check_password, login_user, logout_user

urlpatterns = [
    path('/register', register_user, name='register'),
    path('check_username/', check_username, name="check-username"),
    path('check_email/', check_email, name="check-email"),
    path('check_password', check_password, name="check-password"),
    path('/login_user', login_user, name="login_user"),
    path('logout_user', logout_user, name='logout_user')
]
