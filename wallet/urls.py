from django.urls import path

from wallet import views

urlpatterns = [
    path('welcome/', views.welcome, name='index'),
    path('greet/<str:name>',views.greeting,name='greet'),
]