from django.urls import path
from .views import index, BBLoginView, profile, RegisterView, createapl, aplication, delete
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', index, name='index'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', aplication, name='profile'),
    path('create_aplication/', createapl, name='createapl'),
    path('profile/<int:id>', delete, name='delete'),
    path('profile/<int:id>', delete, name='delete'),

]
