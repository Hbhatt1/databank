from django.forms import ModelForm
from django.forms import forms
from .cell_counts import *
from .models import Participant
from .models import Result
from .models import Study


class StudyForm(ModelForm):
    error_messages = {
        'duplicate_identifier': "A study with that identifier already exists.",
    }

    class Meta:
        model = Study
        fields = ['study_name', 'identifier', 'created_date']

    def clean_identifier(self):
        identifier = self.cleaned_data['identifier']
        try:
            Study.objects.get(identifier=identifier)
        except Study.DoesNotExist:
            return identifier
        raise forms.ValidationError(self.error_messages['duplicate_identifier'])


class ParticipantForm(ModelForm):
    error_messages = {
        'duplicate_participant_identifier': "A participant with that identifier already exists.",
    }

    class Meta:
        model = Participant
        fields = ['participant_identifier', 'registration_date']

    def clean_participant_identifier(self):
        participant_identifier = self.cleaned_data['participant_identifier']
        try:
            Participant.objects.get(participant_identifier=participant_identifier)
        except Participant.DoesNotExist:
            return participant_identifier
        raise forms.ValidationError(self.error_messages['duplicate_participant_identifier'])

# Need a clean function for regular experssion e.g. Test Study TS001 regular expression sets that
# the participant identifier must always be TS followed by a set amount of numbers. The function would then
# pull the participant_identifier and experssion into a function give a True or False to throw a ValidationError
# similar to below clean function

class ResultForm(ModelForm):
    error_messages = {
        'sum_raw': "The sum of the raw sputum counts does not add up to the total cells counted",
    }

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
            'viability',
            'squamcont',
            'tcc',
        ]

    def clean_total_cells(self):
        neut = self.cleaned_data['raw_neutrophils']
        mac = self.cleaned_data['raw_macrophages']
        eos = self.cleaned_data['raw_eosinophils']
        epi = self.cleaned_data['raw_epithelium']
        lym  = self.cleaned_data['raw_lymphocytes']
        total = self.cleaned_data['total_cells']
        total_cells = are_sum_cell_counts_equal_total(neut, mac, eos, epi, lym, total)
        if total_cells == False:
            raise forms.ValidationError(self.error_messages['sum_raw'])
        else:
            return total

# Modfy HTML for date using widgets
