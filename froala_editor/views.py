from django.views.decorators.csrf import csrf_exempt
import json
# from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
import uuid
import os


@csrf_exempt
def image_upload(request):
    if 'file' in request.FILES:
        file = request.FILES['file']
        allowed_types = ['image/jpeg', 'image/jpg', 'image/pjpeg', 'image/x-png', 'image/png', 'image/gif']
        if not file.content_type in allowed_types:
            return HttpResponse(json.dumps({}), mimetype="application/json")
        # Other data on the request.FILES dictionary:
        #   filesize = len(file['content'])
        #   filetype = file['content-type']
        media_root = getattr(settings, 'MEDIA_ROOT', '.')
        media_url = getattr(settings, 'MEDIA_URL', '.')
        upload_to = getattr(settings, 'FROALA_UPLOAD_PATH', 'uploads/froala_editor/images')
        full_upload_path = '%s/%s' % (media_root, upload_to)
        if not os.path.exists(full_upload_path):
            os.makedirs(full_upload_path)
        ext = file.name.split('.')[-1]
        file_name = "%s.%s" % (uuid.uuid4(), ext)
        path = '%s/%s' % (full_upload_path, file_name)
        fd = open(path, 'wb')
        for chunk in file.chunks():
            fd.write(chunk)
        fd.close()
        link = '%s%s/%s' % (media_url, upload_to, file_name)
        # return JsonResponse({'link': link})
        return HttpResponse(json.dumps({'link': link}), content_type="application/json")
