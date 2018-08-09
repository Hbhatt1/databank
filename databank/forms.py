from django.forms import ModelForm
from .models import Study
from django.core.exceptions import ValidationError

class CreateStudyForm(ModelForm):

    class Meta:
         model = Study
         fields = '__all__'
