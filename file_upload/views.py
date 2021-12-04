from django.shortcuts import render, redirect

from .models import Document
from .forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'file_upload/home.html', {'documents': documents})


def file_upload_via_model_form(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_upload:home')
    else:
        form = DocumentForm()
    return render(request, 'file_upload/file_upload.html', {
        'form': form
    })
