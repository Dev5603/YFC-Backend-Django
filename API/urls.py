from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.users),
    path('offers/', views.offers),
    path('offers/<str:name>/', views.offer),
    path('plans/', views.plans),
    path('plans/<str:name>/', views.plan),
    path('blogs', views.blogs),
    path('blogs/<str:title>/', views.blog),
    path('addComment/<int:id>', views.addComment)
]