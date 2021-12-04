from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render
from django.utils.translation import gettext as _

from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        """

        """
        model = Document
        fields = ('description', 'location',)

    def clean(self):
        """
        For validating the form.
        This method will check, is the user trying to upload the same file again
        and return an Error message if any file exists in the database with same
        name.
        :return:
        """
        file_name = str(self.cleaned_data['location'])
        if Document.objects.filter(location='file_upload_assets/' + file_name).exists():
            message = _(f'There is already a file named {file_name} on our system, Please try to upload another file')
            raise ValidationError(message)
