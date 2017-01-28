Django Froala WYSIWYG Editor
============================

    django-froala-editor package helps integrate `Froala WYSIWYG HTML
    editor <https://froala.com/wysiwyg-editor/>`__ with Django.

Getting started
---------------

1. Install the package:

``pip install django-froala-editor``

OR

Add the directory ``froala_editor`` from this repo to your Python path.

1. Add ``froala_editor`` to INSTALLED\_APPS in ``settings.py``.

2. Add the following line to ``urlpatterns`` in your application's
   ``urls.py``.

.. code:: python

      url(r'^froala_editor/', include('froala_editor.urls')),

Skip this url inclusion if you don't want image and file upload inside
WYSIWYG editor. Images from URLs can still be embedded.

Usage
-----

.. code:: python

    from django.db import models
    from froala_editor.fields import FroalaField

    class Page(models.Model):
      content = FroalaField()

``FroalaField`` uses ``froala_editor.widgets.FroalaEditor`` as its
widget. You may directly use this widget with any of your forms.py:

.. code:: python

    from django import forms
    from froala_editor.widgets import FroalaEditor

    class PageForm(forms.ModelForm):
      content = forms.CharField(widget=FroalaEditor)

Usage outside admin
~~~~~~~~~~~~~~~~~~~

When used outside the Django admin, the media files are to be manually
included in the template. Inside the ``<head>`` section or before the
form is rendered, include:

.. code:: python

      {{ form.media }}

In case of jQuery conflict (when your project template already has
jQuery), you need to include the following files instead of
``{{ form.media }}`` plus the static files for theme (if not default)
and required plugins.

.. code:: python

      <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css" type="text/css" media="all" rel="stylesheet" />
      <link href="{{STATIC_URL}}froala_editor/css/froala_editor.min.css" type="text/css" media="all" rel="stylesheet" />
      <link href="{{STATIC_URL}}froala_editor/css/froala_style.min.css" type="text/css" media="all" rel="stylesheet" />
      <script type="text/javascript" src="{{STATIC_URL}}froala_editor/js/froala_editor.min.js"></script>

Or simply, you may use the following in your ``settings.py`` if you
don't want Froala to include jQuery by itself, thus preventing any
conflicts:

.. code:: python

      FROALA_INCLUDE_JQUERY = False

Options
~~~~~~~

Froala Editor provides several options for customizing the editor. See
https://froala.com/wysiwyg-editor/docs for all available options. You
can provide a dictionary of these options as ``FROALA_EDITOR_OPTIONS``
setting in ``settings.py``. These options would then be used for all
instances of the WYSIWYG editor in the project.

Options for individual field can also be provided via ``FroalaField`` or
``FroalaEditor`` class. This overrides any options set via
``FROALA_EDITOR_OPTIONS``:

.. code:: python

    from django.db import models
    from froala_editor.fields import FroalaField

    class Page(models.Model):
      content = FroalaField(options={
        'toolbarInline': True,
      })

.. code:: python

    from django import forms
    from froala_editor.widgets import FroalaEditor

    class PageForm(forms.ModelForm):
      content = forms.TextField(widget=FroalaEditor(options={
        'toolbarInline': True,
      }))

Theme
~~~~~

You may provide the name of the theme to be used as ``theme`` argument
to ``FroalaField`` or ``FroalaEditor``.

.. code:: python

    from django.db import models
    from froala_editor.fields import FroalaField

    class Page(models.Model):
      content = FroalaField(theme='dark')

``FROALA_EDITOR_THEME`` can be set in ``settings.py`` making all
instances of the editor to use a theme. However, ``theme`` argument in
``FroalaField`` and ``FroalaEditor`` overrides ``FROALA_EDITOR_THEME``.
Using a theme named 'dark' would require the existence of the file
``froala_editor/static/froala_editor/css/themes/dark.min.css``.
Available themes are: 'dark', 'gray' and 'red'.

Plugins
~~~~~~~

Froala Editor comes with the plugins: block style, text & background
colors, font size, font family, insert video, insert table, media
manager, lists and file upload. By default, all plugins are enabled by
default in this package. See
https://froala.com/wysiwyg-editor/docs/plugins for all available
plugins.

``FROALA_EDITOR_PLUGINS`` can be set in ``settings.py`` to tell which
plugins should all instances of Froala Editor be using. By default, it
is

.. code:: python

    FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier' ,'code_view', 'colors', 'draggable', 'emoticons',
            'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image_manager', 'image', 'inline_style',
            'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert', 'quote', 'save', 'table',
            'url', 'video')

The usage of ``plugins`` argument with ``FroalaEditor`` or
``FroalaField`` overrides this for that particular instance.

.. code:: python

    from django.db import models
    from froala_editor.fields import FroalaField

    class Page(models.Model):
      content = FroalaField(plugins=('font_size', 'font_family'))

Image upload
~~~~~~~~~~~~

``FroalaEditor`` and ``FroalaField`` optionally take in a boolean value
for ``image_upload`` argument to enable or disable image uploads. Image
uploads are enabled by default if the urls of this package are included
in your urls.py.

You can use ``FROALA_UPLOAD_PATH`` setting in ``settings.py`` to change
the path where uploaded files are stored within the ``MEDIA_ROOT``. By
default, ``uploads/froala_editor/images`` is used for storing uploaded
images.

Include jQuery
~~~~~~~~~~~~~~

jQuery is included by default in form media. If you don't want to
include jQuery, you may pass ``include_jquery=False`` to
``FroalaEditor`` or ``FroalaField``. ``FROALA_INCLUDE_JQUERY`` can be
also set in ``settings.py`` for project wide effects.

License
-------

This package is available under BSD License. However, in order to use
Froala WYSIWYG HTML Editor plugin you should purchase a license for it.

See https://froala.com/wysiwyg-editor/pricing for licensing the Froala
Editor.

If you bought a license and got your key, the easiest way to implement
it is to put it into the ``FROALA_EDITOR_OPTIONS`` setting in
``settings.py``:

\`\`\`python FROALA\_EDITOR\_OPTIONS = { 'key': '', # other options #
... }
