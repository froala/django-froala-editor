from django.db.models import Field
from froala_editor.widgets import FroalaEditor
from django.conf import settings


class FroalaField(Field):
    description = "Froala Editable Field"

    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options', {})
        self.theme = kwargs.pop('theme', getattr(settings, 'FROALA_EDITOR_THEME', None))
        self.plugins = kwargs.pop('plugins', getattr(settings, 'FROALA_EDITOR_PLUGINS', (
                                  'font_size', 'font_family', 'colors', 'block_styles', 'video', 'tables', 'media_manager', 'lists', 'file_upload', 'char_counter'
                                  )))
        self.buttons = kwargs.pop('buttons', getattr(settings, 'FROALA_EDITOR_BUTTONS', (
            'bold', 'italic', 'underline', 'strikeThrough', 'font_size', 'font_family', 'colors',
            'sep', 'block_styles', 'blockStyle', 'align', 'lists', 'outdent', 'indent',
            'sep', 'createLink', 'insertImage', 'video', 'media_manager', 'file_upload', 'tables',
            'insertHorizontalRule', 'undo', 'redo', 'html'
        )))
        self.include_jquery = kwargs.pop('include_jquery', getattr(settings, 'FROALA_INCLUDE_JQUERY', True))
        self.image_upload = kwargs.pop('image_upload', True)
        self.file_upload = kwargs.pop('file_upload', True)
        super(FroalaField, self).__init__(*args, **kwargs)

    # TODO Migration for Django 1.7+
    # def deconstruct(self):

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {
            'widget': FroalaEditor(options=self.options, theme=self.theme, buttons=self.buttons, plugins=self.plugins,
                                   include_jquery=self.include_jquery, image_upload=self.image_upload,
                                   file_upload=self.file_upload)}
        defaults.update(kwargs)
        return super(FroalaField, self).formfield(**defaults)


try:
    from south.modelsinspector import add_introspection_rules

    add_introspection_rules([], ["^froala_editor\.fields\.FroalaField"])
except ImportError:
    pass
