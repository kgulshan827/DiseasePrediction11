
from django.urls import path
from .import views
urlpatterns = [
    path('',views.heart,name='heart'),
    path('heart_result/',views.heart_result,name='heart_result')
]
