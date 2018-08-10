from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('studies/', views.studylist, name='studylist'),
    path('studies/add_study', views.add_study, name='add_study'),
    path('studies/<int:id>', views.study_update, name='study_edit')
]
