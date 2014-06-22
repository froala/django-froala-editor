from django.forms import widgets
from django.utils.safestring import mark_safe


class FroalaEditor(widgets.Textarea):
    def __init__(self, *args, **kwargs):
        super(FroalaEditor, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        html = super(FroalaEditor, self).render(name, value, attrs)
        el_id = self.build_attrs(attrs).get('id')
        html += self.trigger_froala(el_id, {})
        # html += self.init_js % (id_, self.get_options())
        return mark_safe(html)

    def trigger_froala(self, el_id, options):
        str = """
        <script>
            $(function(){
                $('#id_content').editable({inlineMode: false, alwaysBlank: true})
            });
        </script>"""
        return str

    class Media:
        css = {
            'all': ('froala_editor/css/font-awesome.min.css', 'froala_editor/css/froala_editor.min.css')
        }
        js = ('js/jquery.js', 'froala_editor/js/froala_editor.min.js',)
