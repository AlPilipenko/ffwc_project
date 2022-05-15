from django.urls import path
from .views import (PersonalPage, TestDetail, InputWeight,
ChangeUserDetails, CustomLoginView, RegisterPage, Group)

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('account/', PersonalPage.as_view(), name='account'),
    path('test/<int:pk>', TestDetail.as_view(), name='test'),
    path('update-weight/', InputWeight.as_view(), name='update-weight'),
    path('update-details/', ChangeUserDetails.as_view(), name='update-details'),

    path('', Group.as_view(), name='group'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
]