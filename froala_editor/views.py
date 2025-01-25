import json
# from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
import os
from django.utils.translation import gettext_lazy as _
from django.utils.module_loading import import_string


# Allow for a custom storage backend defined in settings.
def get_storage_class():
    return import_string(getattr(settings, 'FROALA_STORAGE_BACKEND', 'django.core.files.storage.DefaultStorage'))()


storage = get_storage_class()


def image_upload(request):
    if 'file' in request.FILES:
        the_file = request.FILES['file']
        allowed_types = [
            'image/jpeg',
            'image/jpg',
            'image/pjpeg',
            'image/x-png',
            'image/png',
            'image/gif'
        ]
        if not the_file.content_type in allowed_types:
            return HttpResponse(json.dumps({'error': _('You can only upload images.')}),
                                content_type="application/json")
        upload_to = getattr(settings, 'FROALA_UPLOAD_PATH', 'uploads/froala_editor/images/')
        path = storage.save(os.path.join(upload_to, the_file.name), the_file)
        link = request.build_absolute_uri(storage.url(path))

        return HttpResponse(json.dumps({'link': link}), content_type="application/json")


def file_upload(request):
    if 'file' in request.FILES:
        the_file = request.FILES['file']
        upload_to = getattr(settings, 'FROALA_UPLOAD_PATH', 'uploads/froala_editor/files/')
        path = storage.save(os.path.join(upload_to, the_file.name), the_file)
        link = storage.url(path)
        return HttpResponse(json.dumps({'link': link}), content_type="application/json")


def video_upload(request):
    if 'file' in request.FILES:
        the_file = request.FILES['file']
        allowed_types = [
            'video/mp4',
            'video/webm',
            'video/ogg',
        ]
        if not the_file.content_type in allowed_types:
            return HttpResponse(json.dumps({'error': _('You can only upload videos.')}), content_type="application/json")
        upload_to = getattr(settings, 'FROALA_UPLOAD_PATH', 'uploads/froala_editor/videos/')
        path = storage.save(os.path.join(upload_to, the_file.name), the_file)
        link = request.build_absolute_uri(storage.url(path))

        return HttpResponse(json.dumps({'link': link}), content_type="application/json")
