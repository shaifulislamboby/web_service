from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from file_upload import models as m


class DocumentAdmin(ImportExportModelAdmin):
    """
    Making file field readonly in the Django admin interface,
    As we are saving the file details once any Document object
    is created, so we do not want to give the user the ability
    to change the file itself.
    """
    readonly_fields = ('file',)
    search_fields = ['description', 'file']

    def has_add_permission(self, request, obj=None):
        """
        Overriding the add new instance permission.
        As we only want to add new files via Django form
        :param request:
        :param obj:
        :return:
        """
        return False


admin.site.register(m.Document, DocumentAdmin)

