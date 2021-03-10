
from django.urls import path
from .import views

urlpatterns = [
    path('',views.diabetes,name="diabetes"),
    path('diabetes_result/',views.diabetes_result,name="diabetes_result")
]
