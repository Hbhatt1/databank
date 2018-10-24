from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Result)
class ResultsAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Study)
admin.site.register(Participant)
