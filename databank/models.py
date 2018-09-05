from django.db import models
from django.utils import timezone
import datetime

class Study(models.Model):
    study_name = models.CharField(max_length=100, blank=False, unique=True)
    identifier = models.CharField(max_length=10, blank=False)
    created_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return '%s' % self.study_name


class Participant(models.Model):
    study = models.ForeignKey(Study, on_delete=models.PROTECT)
    participant_identifier = models.CharField(max_length=10, blank=False)
    registration_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return '%s' % self.participant_identifier


class Result(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.PROTECT)
    participant_identifier = models.CharField(max_length=10, blank=False)
    visit_number = models.CharField(max_length=10, blank=False)
    visit_date = models.DateField(default=datetime.date.today)
    raw_neutrophils = models.CharField(max_length=3, blank=False)
    raw_macrophages = models.CharField(max_length=3, blank=False)
    raw_eosinophils = models.CharField(max_length=3, blank=False)
    raw_epithelium = models.CharField(max_length=3, blank=False)
    raw_lymphocytes = models.CharField(max_length=3, blank=False)

    def __str__(self):
        return '%s' % self.participant_identifier

# override save function here to do the calculation
