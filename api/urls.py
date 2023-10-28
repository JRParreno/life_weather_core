from django.urls import path
from django.contrib.auth import views as auth_views

from user_profile.views import (ProfileView,
                                RegisterView, ChangePasswordView, UploadPhotoView, RequestPasswordResetEmail)
from journal.views import (TodoListCreateView, TodoRetrieveUpdateDestroyView)

app_name = 'api'

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('upload-photo/<pk>', UploadPhotoView.as_view(), name='upload-photo'),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),

    path('forgot-password', RequestPasswordResetEmail.as_view(),
         name='forgot-password '),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password-reset-confirm'),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),

    path('todo/list', TodoListCreateView.as_view(), name='todo-list'),
    path('todo/<pk>', TodoRetrieveUpdateDestroyView.as_view(),
         name='todo-update-retrieve-destroy'),
]
