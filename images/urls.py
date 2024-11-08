from django.urls import path

from images import views

urlpatterns = [
    path('', views.image_list, name='image'),
]