from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('study_list/', views.studylist, name='studylist'),
    path('study_list/add_study', views.add_study, name='add_study')
]
