from django.db import models
from django.utils import timezone
# Create your models here.

class Study(models.Model):
    study_name = models.CharField(max_length=100, blank=False)
    identifier = models.CharField(max_length=10, blank=False)
    created_date = models.DateTimeField(default=timezone.now)


class Participant(models.Model):
    study = models.ForeignKey(Study, on_delete=models.PROTECT)
    registration_date = models.DateTimeField(default=timezone.now)


class Result(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.PROTECT)
    visit_number = models.CharField(max_length=10, blank=False)
    visit_date = models.DateTimeField('date of visit')
    raw_neutrophils = models.CharField(max_length=3, blank=False)
    raw_macrophages = models.CharField(max_length=3, blank=False)
    raw_eosinophils = models.CharField(max_length=3, blank=False)
    raw_epithelium = models.CharField(max_length=3, blank=False)
    raw_lymphocytes = models.CharField(max_length=3, blank=False)
