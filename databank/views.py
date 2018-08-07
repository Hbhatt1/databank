from django.shortcuts import render
from django.utils import timezone
from databank.models import Study

# Create your views here.
def homepage(request):
    return render(request, 'databank/homepage.html')

def studylist(request):
    return render(request, 'databank/study_list.html',
    {'studylist':Study.objects.all})
