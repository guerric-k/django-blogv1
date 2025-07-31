from . import views
from django.urls import path

# URL patterns for the blog app
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]