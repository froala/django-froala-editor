from django.core.urlresolvers import reverse, NoReverseMatch
from django.forms import widgets, Media
from django.utils.safestring import mark_safe
from django.conf import settings
import json


class FroalaEditor(widgets.Textarea):
    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options', {})
        self.plugins = kwargs.pop('plugins', getattr(settings, 'FROALA_EDITOR_PLUGINS', (
            'font_size', 'font_family', 'colors', 'block_styles', 'video', 'tables', 'media_manager', 'lists',
            'file_upload'
        )))
        self.theme = kwargs.pop('theme', getattr(settings, 'FROALA_EDITOR_THEME', None))
        self.include_jquery = kwargs.pop('include_jquery', getattr(settings, 'FROALA_INCLUDE_JQUERY', True))
        self.image_upload = kwargs.pop('image_upload', True)
        self.file_upload = kwargs.pop('file_upload', True)
        super(FroalaEditor, self).__init__(*args, **kwargs)

    def get_options(self):

        default_options = {
            'inlineMode': False,
        }

        try:
            image_upload_url = reverse('froala_editor_image_upload')
            default_options['imageUploadURL'] = image_upload_url
            default_options.update([('imageUploadParams', {'csrfmiddlewaretoken': 'csrftokenplaceholder'})])
        except NoReverseMatch:
            default_options['imageUpload'] = False
        settings_options = getattr(settings, 'FROALA_EDITOR_OPTIONS', {})
        # options = dict(default_options.items() + settings_options.items() + self.options.items())
        options = dict(default_options.items()).copy()
        options.update(settings_options.items())
        options.update(self.options.items())


        if self.theme:
            options['theme'] = self.theme

        json_options = json.dumps(options)
        json_options = json_options.replace('"csrftokenplaceholder"', 'getCookie("csrftoken")')
        return json_options


    def render(self, name, value, attrs=None):
        html = super(FroalaEditor, self).render(name, value, attrs)
        el_id = self.build_attrs(attrs).get('id')
        html += self.trigger_froala(el_id, self.get_options())
        return mark_safe(html)

    def trigger_froala(self, el_id, options):

        str = """
        <script>
            $(function(){
                $('#%s').editable(%s)
            });
        </script>""" % (el_id, options)
        return str

    def _media(self):
        css = {
            'all': ('froala_editor/css/font-awesome.min.css', 'froala_editor/css/froala_editor.min.css',
                    'froala_editor/css/froala_style.min.css', 'froala_editor/css/froala-django.css')
        }
        js = ('froala_editor/js/froala_editor.min.js','froala_editor/js/froala-django.js',)

        if self.include_jquery:
            js = ('froala_editor/js/libs/jquery-1.11.1.min.js',) + js

        if self.theme:
            css['all'] += ('froala_editor/css/themes/' + self.theme + '.css',)

        for plugin in self.plugins:
            js += ('froala_editor/js/plugins/' + plugin + '.min.js',)

        return Media(css=css, js=js)

    media = property(_media)
