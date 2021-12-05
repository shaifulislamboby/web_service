import factory


class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'file_upload.Document'

    description = 'Test'
    file = 'test__.txt'


class FileDetailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'api_services.FileDetail'

    line_number = 11
    line_content = 'Test is going on'
    line_length = 16
    most_occurred_letter = 'a'
    document = factory.SubFactory(DocumentFactory)
