from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView
from django.urls import reverse
from databank.models import Study
from databank.models import Participant
from databank.models import Result
from .forms import StudyForm
from .forms import ParticipantForm
from .forms import ResultForm

# Homepage
def homepage(request):
    return render(request, 'databank/homepage.html')


# Shows studies with add and edit capabilities
def study_list(request):
    return render(request, 'databank/studies.html',
    {'study_list':Study.objects.all})

def add_study(request):
    if request.method == "POST":
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('study_list'))
    else:
        form = StudyForm()
    return render(request, 'studies/add_study.html', {'form': form})

def edit_study(request, study_id, template_name='studies/edit_study.html'):
    study = get_object_or_404(Study, id=study_id)
    form = StudyForm(request.POST or None, instance=study)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('study_list'))
    return render(request, template_name, {'form':form})


# Shows participants related to a study with add and edit capabilities
def participant_list(request, study_id, template_name='databank/participants.html'):
    participants = Participant.objects.filter(study_id=study_id)
    return render(request, template_name, {'participant_list':participants, 'study_id':study_id})

def add_participant(request, study_id, template_name ='studies/add_participant.html' ):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant_item = form.save(commit=False)
            participant_item.study_id = study_id
            participant_item.save()
            return HttpResponseRedirect(reverse('participant_list', args=(study_id,)))
    else:
        form = ParticipantForm()
    return render(request, template_name, {'form': form, 'study_id': study_id})

def edit_participant(request, study_id, participant_id, template_name='studies/edit_participant.html'):
    participant = get_object_or_404(Participant, id=participant_id)
    form = ParticipantForm(request.POST or None, instance=participant)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('participant_list', args=(study_id,)))
    return render(request, template_name, {'form': form, 'study_id':study_id, 'participant_id':participant_id})


# Shows Results linked to participant related to a study with add and edit capabilities
def result(request, study_id, participant_id, template_name='databank/results.html'):
    results = Result.objects.filter(participant_id=participant_id)
    return render(request, template_name, {'results':results, 'participant_id':participant_id, 'study_id':study_id})

def add_result(request, study_id, participant_id, template_name='studies/add_result.html'):
    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            result_item = form.save(commit=False)
            result_item.result_id = participant_id
            participant_item.save()
            return HttpResponseRedirect(reverse('results', args=(participant_id,)))
    else:
        form = ResultForm()
    return render(request, template_name, {'form': form, 'study_id':study_id, 'participant_id':participant_id})
