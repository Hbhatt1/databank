from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('studies/', views.study_list, name='study_list'),
    path('studies/add_study', views.add_study, name='add_study'),
    path('studies/<int:study_id>', views.edit_study, name='edit_study'),
    path('studies/<int:study_id>/participants', views.participant_list, name='participant_list'),
    path('studies/<int:study_id>/participants/add_participant', views.add_participant, name='add_participant'),
    path('studies/<int:study_id>/participants/<int:participant_id>', views.edit_participant, name='edit_participant'),
    path('studies/<int:study_id>/participants/<int:participant_id>/result', views.result, name='results'),
    path('studies/<int:study_id>/participants/<int:participant_id>/result/add_result', views.add_result, name='add_result')
]
