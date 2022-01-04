from django.core.exceptions import ValidationError
from django import forms
from django.core.mail import send_mail
from django.utils.translation import ugettext as _

from .models import Document


class DocumentForm(forms.ModelForm):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

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

    def send_email(self):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        sender = self.cleaned_data['sender']
        cc_myself = self.cleaned_data['cc_myself']

        recipients = ['shaifulislamopu@gmail.com']
        if cc_myself:
            recipients.append(sender)
        send_mail(subject, message, sender, recipients)
