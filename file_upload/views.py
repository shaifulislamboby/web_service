from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .models import Document
from .forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'file_upload/home.html', {'documents': documents})


# def file_upload_via_model_form(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('file_upload:home')
#     else:
#         form = DocumentForm()
#     return render(request, 'file_upload/file_upload.html', {
#         'form': form
#     })


class FileUpload(FormView):
    template_name = 'file_upload/file_upload.html'
    form_class = DocumentForm
    success_url = reverse_lazy('file_upload:home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
