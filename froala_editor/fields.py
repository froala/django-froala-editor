from django.db.models import Field
from froala_editor.widgets import FroalaEditor


class FroalaField(Field):
    description = "Froala Editable Field"

    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options', {})
        self.image_upload = kwargs.pop('image_upload', True)
        self.file_upload = kwargs.pop('file_upload', True)
        super(FroalaField, self).__init__(*args, **kwargs)

    # TODO Migration for Django 1.7+
    # def deconstruct(self):

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {
            'widget': FroalaEditor(options=self.options, image_upload=self.image_upload, file_upload=self.file_upload)}
        defaults.update(kwargs)
        return super(FroalaField, self).formfield(**defaults)


try:
    from south.modelsinspector import add_introspection_rules

    add_introspection_rules([], ["^froala_editor\.fields\.FroalaField"])
except ImportError:
    pass