from django.urls import path
from api import views

urlpatterns = [
    path('home',views.home),
    path('getStudent',views.getStudent),
    path('registerStudent',views.registerStudent)
]