from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView
from django.urls import reverse
from databank.models import Study
from .forms import StudyForm

# Create your views here.
def homepage(request):
    return render(request, 'databank/homepage.html')


def studylist(request):
    return render(request, 'databank/studies.html',
    {'studylist':Study.objects.all})


def add_study(request):
    if request.method == "POST":
        form = StudyForm(request.POST)
        if form.is_valid():
            study_item = form.save(commit=False)
            study_item.save()
            return HttpResponseRedirect(reverse('studylist'))
    else:
        form = StudyForm()
    return render(request, 'studies/add_study.html', {'form': form})


def study_update(request, id, template_name='studies/add_study.html'):
    study = get_object_or_404(Study, id=id)
    form = StudyForm(request.POST or None, instance=study)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('studylist'))
    return render(request, template_name, {'form':form})
