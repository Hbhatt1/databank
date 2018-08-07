from django.contrib import admin
from .models import Study
from .models import Participant
from .models import Result
# Register your models here.

admin.site.register(Study)
admin.site.register(Participant)
admin.site.register(Result)
