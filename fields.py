from django.db.models import Field, TextField, CharField
from django.conf import settings
from froala_editor.widgets import FroalaEditor


class FroalaField(Field):
    # def __init__(self, *args, **kwargs):
    #     self.widget = FroalaEditor()
    #     super(FroalaField, self).__init__(*args, **kwargs)

    # TODO Migration for Django 1.7+
    # def deconstruct(self):

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {'widget': FroalaEditor()}
        defaults.update(kwargs)
        return super(FroalaField, self).formfield(**defaults)


try:
    from south.modelsinspector import add_introspection_rules

    add_introspection_rules([], ["^froala_editor\.fields\.FroalaField"])
except ImportError:
    pass