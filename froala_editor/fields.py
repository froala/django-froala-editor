from django.db.models import Field, TextField, CharField
from django.conf import settings
from froala_editor.widgets import FroalaEditor
from django.forms import widgets


class FroalaField(Field):
    description = "Froala Editable Field"

    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options', {})
        super(FroalaField, self).__init__(*args, **kwargs)

    # TODO Migration for Django 1.7+
    # def deconstruct(self):

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {'widget': FroalaEditor(options=self.options)}
        defaults.update(kwargs)
        return super(FroalaField, self).formfield(**defaults)


try:
    from south.modelsinspector import add_introspection_rules

    add_introspection_rules([], ["^froala_editor\.fields\.FroalaField"])
except ImportError:
    pass