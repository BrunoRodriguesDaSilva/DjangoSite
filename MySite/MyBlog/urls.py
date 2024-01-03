from django.urls import path

from MyBlog import views


urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
]