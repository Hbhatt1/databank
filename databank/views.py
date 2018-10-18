from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as db_login, logout
from django.contrib.auth.models import User
from django.contrib import auth
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

# Register, Login and Logout

def register(request):
    if request.method =="POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'databank/register.html', {'error':'Username already exists!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('homepage')
        else:
            return render(request, 'databank/register.html', {'error':'Passwords must match!'})
    else:
        return render(request, 'databank/register.html')

def login(request):
    if request.method =="POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            db_login(request, user)
            return redirect('study_list')
        else:
            return render(request, 'databank/login.html', {'error':'Username or password is incorrect'})
    else:
        return render(request, 'databank/login.html')

def logout(request):
    if request.method =="POST":
        auth.logout(request)
        return redirect('homepage')


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
            result_item.participant_id = participant_id
            result_item.save()
            return HttpResponseRedirect(reverse('results', args=(study_id, participant_id,)))
    else:
        form = ResultForm()
    return render(request, template_name, {'form': form, 'study_id':study_id, 'participant_id':participant_id})

def edit_result(request, study_id, participant_id, result_id, template_name='studies/edit_results.html'):
    result = get_object_or_404(Result, id=result_id)
    form = ResultForm(request.POST or None, instance=result)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('results', args=(study_id, participant_id,)))
    return render(request, template_name, {'form':form, 'study_id':study_id, 'participant_id':participant_id, 'result_id':result_id})
