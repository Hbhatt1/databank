from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from databank.models import Study
from .forms import CreateStudyForm

# Create your views here.
def homepage(request):
    return render(request, 'databank/homepage.html')

def studylist(request):
    return render(request, 'databank/study_list.html',
    {'studylist':Study.objects.all})

def add_study(request):
    if request.method == "POST":
        form = CreateStudyForm(request.POST)
        if form.is_valid():
            study_item = form.save(commit=False)
            study_item.save()
            return HttpResponseRedirect(reverse('studylist'))
            #django.messages
            #httpresponse
    else:
        form = CreateStudyForm()
    return render(request, 'study_list/add_study.html', {'form': form})
