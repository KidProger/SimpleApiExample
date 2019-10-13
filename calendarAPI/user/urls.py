from django.urls import path

from user.views import UserRegistrationView, UsersListView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('users_list/', UsersListView.as_view(), name='users_list'),
]