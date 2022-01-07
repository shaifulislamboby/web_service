from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .models import Document
from .forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    if documents:
        return render(request, 'file_upload/home.html', {'documents': documents})
    return render(request, 'file_upload/home.html', {'documents': ''})


class FileUpload(FormView):
    template_name = 'file_upload/file_upload.html'
    form_class = DocumentForm
    success_url = reverse_lazy('file_upload:home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
