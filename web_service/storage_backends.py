from storages.backends.s3boto3 import S3Boto3Storage



class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False


class MediaAttachmentStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

    def get_object_parameters(self, name):
        return {'ContentDisposition': 'attachment'}
