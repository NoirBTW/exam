from django.urls import path
from .views import asexam_list

urlpatterns = [
    path('asexam/', asexam_list, name='asexam_list'),
] 