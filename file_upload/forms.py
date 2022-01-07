from django.core.exceptions import ValidationError
from django import forms
from django.core.mail import send_mail
from django.utils.translation import ugettext as _

from .models import Document


class DocumentForm(forms.ModelForm):

    class Meta:
        """
        Form class which will be shown for the file upload
        The form will have 2 fields
        1. Description or details about the file that being uploaded.
        2. The file name/ file itself.

        """
        model = Document
        fields = ('description', 'file',)

    def clean(self):
        """
        For validating the form.
        This method will check, is the user trying to upload the same file again
        and return an Error message if any file exists in the database with same
        name.
        :return:
        """
        file_name = str(self.cleaned_data['file'])
        if Document.objects.filter(file__exact='file_upload_assets/' + file_name).exists():
            message = _('There is already a file with same name on our system, Please try to upload another file')
            raise ValidationError(message)

