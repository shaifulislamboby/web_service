from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from api_services import models as m


class FileDetailAdmin(ImportExportModelAdmin):
    """
    Here all the fields can be modified by admin user
    so no read only field.
    """
    search_fields = ['line_content', 'line_length']


admin.site.register(m.FileDetail, FileDetailAdmin)
