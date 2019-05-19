from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('users/<int:pk>/confirmation/',
         views.UserConfirmation.as_view(), name='user-confirmation'),
]
