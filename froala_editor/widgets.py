from django.forms import widgets
from django.utils.safestring import mark_safe
from django.conf import settings
import json


class FroalaEditor(widgets.Textarea):
    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options', {})
        super(FroalaEditor, self).__init__(*args, **kwargs)

    def get_options(self):
        default_options = {
            'inlineMode': False,
        }
        settings_options = getattr(settings, 'FROALA_EDITOR_OPTIONS', {})
        options = dict(default_options.items() + settings_options.items() + self.options.items())
        return json.dumps(options)


    def render(self, name, value, attrs=None):
        html = super(FroalaEditor, self).render(name, value, attrs)
        el_id = self.build_attrs(attrs).get('id')
        html += self.trigger_froala(el_id, self.get_options())
        # html += self.init_js % (id_, self.get_options())
        # html = '<br>' + html
        return mark_safe(html)

    def trigger_froala(self, el_id, options):
        str = """
        <script>
            $(function(){
                $('#%s').editable(%s)
            });
        </script>""" % (el_id, options)
        return str

    class Media:
        css = {
            'all': ('froala_editor/css/font-awesome.min.css', 'froala_editor/css/froala_editor.min.css')
        }
        js = ('js/jquery.js', 'froala_editor/js/froala_editor.min.js',)
