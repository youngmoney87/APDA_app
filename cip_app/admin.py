from django.contrib import admin
from .models import SchoolList, ConversionSheet


# Register your models here.
def export_to_csv(modeladmin, request, queryset):
    meter_ids = [x.meter_id for x in queryset]
    if len(meter_ids) < 1:
        modeladmin.message_user(request, 'Must select some records first')
        return


class SchoolListAdmin(admin.ModelAdmin):
    list_display = [
       'unitid',
        'school',
        'client',
    ]
    # list_filter = [MeterIsFMPFilter, MeterResponsibleCompanyFilter,  MeterIsActiveFilter, MeterBasinFilter]
    actions = [export_to_csv, ]
    search_fields = ['SCHOOL', 'Client']
    list_editable = [
    #    'unitid',
        'school',
        'client',
    ]

    # ordering = ['basin', '`meter_id', ]

    def get_actions(self, request):
        actions = super(SchoolListAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(SchoolList, SchoolListAdmin)
admin.site.register(ConversionSheet)