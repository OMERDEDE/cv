from django.urls import path

from . import views
from django.contrib import admin
from django.urls import path

from django.urls import path
from .views import DisplayPages
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #DISPLAY PAGES
    path('', views.DisplayPages.login, name='main'),
    path('login', views.DisplayPages.login_page, name='main'),
    path('homepage/', views.DisplayPages.homepage, name='homepage'),
    path('register/', views.DisplayPages.register, name='register'),
    path('cv_detail/<int:cv_id>/', views.DisplayPages.cv_detail, name='cv_detail'),
    path('update_cv/<int:cv_id>/', views.DisplayPages.update_cv, name='update_cv'),
    path('update_cv/<int:cv_id>', views.DisplayPages.update_cv, name='update_cv'),
    path('cv_all', views.DisplayPages.cvall, name='cvpage'),
    path('create_cv', views.DisplayPages.cvcreate, name='cvpage'),
    path('cv_create', views.DisplayPages.cv_create, name='cv_create'),
    path('cv_adjust', views.DisplayPages.cv_adjust, name='cv_adjust'),
    path('submit_comment', views.DisplayPages.submit_comment, name='submit_comment'),
    path('comments', views.DisplayPages.comments, name='comments'),
]
