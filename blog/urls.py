from . import views
from django.urls import path

# URL patterns for the blog app
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
     path('<slug:slug>/', views.post_detail, name='post_detail'),
]