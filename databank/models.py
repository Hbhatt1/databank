from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from databank.utils import raw_to_percentage
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
    visit_number = models.CharField(max_length=10, blank=False)
    visit_date = models.DateField(default=datetime.date.today)
    raw_neutrophils = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(400)], null=True)
    raw_macrophages = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(400)], null=True)
    raw_eosinophils = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(400)], null=True)
    raw_epithelium = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(400)], null=True)
    raw_lymphocytes = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(400)], null=True)
    total_cells = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(400)], null=True)
    percent_neutrophils = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    percent_macrophages = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    percent_eosinophils = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    percent_epithelium = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    percent_lymphocytes = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)

    def __str__(self):
        return '%s' % self.participant

# Override save function: When add result POST - import raw_to_percentage function in from utlis
# and feed in the raw values and total cells. Set percent_blah to calculated values using super to
# override result_item.save() in the add_result function of views.py

    def save(self, *args, **kwargs):
        self.percent_neutrophils = raw_to_percentage(self.raw_neutrophils, self.total_cells)
        self.percent_macrophages = raw_to_percentage(self.raw_macrophages, self.total_cells)
        self.percent_eosinophils = raw_to_percentage(self.raw_eosinophils, self.total_cells)
        self.percent_epithelium = raw_to_percentage(self.raw_epithelium, self.total_cells)
        self.percent_lymphocytes = raw_to_percentage(self.raw_lymphocytes, self.total_cells)
        super(Result, self).save(*args, **kwargs)

# Validate raw values total = total cells
# Validate count percentages add up to 100
# Validation for adding multiple Studies, Participant or Results with similar names
# User permissions and logins - page for login
