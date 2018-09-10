from django.forms import ModelForm
from django.forms import forms
from .models import Study
from .models import Participant
from .models import Result
from django.core.exceptions import ValidationError

class StudyForm(ModelForm):

    class Meta:
         model = Study
         fields = '__all__'

class ParticipantForm(ModelForm):

    class Meta:
        model = Participant
        fields = ['participant_identifier', 'registration_date']

class ResultForm(ModelForm):

    class Meta:
        model = Result
        fields = [
        'visit_number',
        'visit_date',
        'raw_neutrophils',
        'raw_macrophages',
        'raw_eosinophils',
        'raw_epithelium',
        'raw_lymphocytes',
        'total_cells',
        ]

# Modfy HTML for date using widgets
# Validators?
