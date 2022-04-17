from django.urls import path
from . import views

urlpatterns = [
    path('projects/get/', views.project_list),
    path('projects/get/<str:pk>/', views.single_project),
    path('projects/post/imagealbum', views.imageAlbum_create),
    path('projects/post/image', views.image_create),
]
