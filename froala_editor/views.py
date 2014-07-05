from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from froala_editor.forms import ImageForm
import json
from django.http import HttpResponse
from django.conf import settings
import uuid



@csrf_exempt
def image_upload(request):
    if request.POST:
        if 'file' in request.FILES:
            file = request.FILES['file']
            # Other data on the request.FILES dictionary:
            #   filesize = len(file['content'])
            #   filetype = file['content-type']
            media_root = getattr(settings, 'MEDIA_ROOT', '.')
            media_url = getattr(settings, 'MEDIA_URL', '.')
            upload_to = getattr(settings, 'FROALA_UPLOAD_PATH', '/uploads/froala_editor/images')
            filename = file.name
            ext = filename.split('.')[-1]
            final_name = "%s.%s" % (uuid.uuid4(), ext)
            path = '%s/%s/%s' % (media_root, upload_to, final_name)
            print path
            fd = open(path, 'wb')
            for chunk in file.chunks():
                fd.write(chunk)
            fd.close()
            url = '%s/%s/%s' % (media_url, upload_to, filename)
            print url
            data = {'link': url}
            return HttpResponse(json.dumps(data), mimetype="application/json")
