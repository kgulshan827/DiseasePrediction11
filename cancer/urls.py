
from django.urls import path
from .import views

urlpatterns = [
    path('',views.cancer,name='cancer'),
    path('cancer_result/',views.cancer_result,name='cancer_result')
]
