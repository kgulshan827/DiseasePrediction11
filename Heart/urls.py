
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('heart/',views.heart,name='heart'),
    path('heart/heart_result/',views.heart_result,name='heart_result')
]
