from django.urls import re_path
from froala_editor import views

urlpatterns = [
    re_path(r'^image_upload/$', views.image_upload, name='froala_editor_image_upload'),
    re_path(r'^file_upload/$', views.file_upload, name='froala_editor_file_upload'),
]
