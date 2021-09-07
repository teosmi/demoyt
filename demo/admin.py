from django.contrib import admin
from demo.models.application import application
from demo.models.product import product
from demo.models.indication import indication
from demo.models.personne import Personne

from import_export.admin import ImportExportModelAdmin

@admin.register(application)
class applicationAdmin(ImportExportModelAdmin):
    pass

@admin.register(product)
class productAdmin(ImportExportModelAdmin):
    pass

@admin.register(indication)
class indicationAdmin(ImportExportModelAdmin):
    pass

@admin.register(Personne)
class indicationAdmin(ImportExportModelAdmin):
    pass