from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('study_list/', views.studylist, name='studylist'),
]
