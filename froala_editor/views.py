import json
# from django.http import JsonResponse
import urlparse
from django.http import HttpResponse
from django.conf import settings
import uuid
import os
from django.core.files.storage import FileSystemStorage


def image_upload(request):
    if 'file' in request.FILES:
        the_file = request.FILES['file']
        allowed_types = ['image/jpeg', 'image/jpg', 'image/pjpeg', 'image/x-png', 'image/png', 'image/gif']
        if not the_file.content_type in allowed_types:
            return HttpResponse(json.dumps({}), content_type="application/json")
        # Other data on the request.FILES dictionary:
        # filesize = len(file['content'])
        # filetype = file['content-type']
        media_root = getattr(settings, 'MEDIA_ROOT', '.')
        media_url = getattr(settings, 'MEDIA_URL', '.')
        upload_to = getattr(settings, 'FROALA_UPLOAD_PATH', 'uploads/froala_editor/images/')
        full_upload_path = '%s/%s' % (media_root, upload_to)
        storage = FileSystemStorage(location=full_upload_path)
        name = storage.save(None, the_file)
        storage.base_url = urlparse.urljoin(media_url, upload_to)
        link = storage.url(name)
        # return JsonResponse({'link': link})
        return HttpResponse(json.dumps({'link': link}), content_type="application/json")
