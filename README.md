# Django Froala WYSIWYG Editor

>django-froala-editor package helps integrate [Froala WYSIWYG HTML editor](https://froala.com/wysiwyg-editor/) with Django.

## Getting started

1. Install the package:

  `pip install django-froala-editor`

  if not update in pypi use this

  `pip install https://github.com/froala/django-froala-editor/archive/master.zip`

OR

Add the directory `froala_editor` from this repo to your Python path.

2. Add `froala_editor` to INSTALLED_APPS in `settings.py`.

3. Add the following line to `urlpatterns` in your application's `urls.py`.

```python
  url(r'^froala_editor/', include('froala_editor.urls')),
```

Skip this url inclusion if you don't want image and file upload inside WYSIWYG editor. Images from URLs can still be embedded.

## Usage

```python
from django.db import models
from froala_editor.fields import FroalaField

class Page(models.Model):
  content = FroalaField()
```

`FroalaField` uses `froala_editor.widgets.FroalaEditor` as its widget. You may directly use this widget with any of your forms.py:

```python
from django import forms
from froala_editor.widgets import FroalaEditor

class PageForm(forms.ModelForm):
  content = forms.CharField(widget=FroalaEditor)
```

### Usage outside admin

When used outside the Django admin, the media files are to be manually included in the template. Inside the ``<head>`` section or before the form is rendered, include:

```python
{{ form.media }}
```

### Options

Froala Editor provides several options for customizing the editor. See [https://froala.com/wysiwyg-editor/docs](https://froala.com/wysiwyg-editor/docs) for all available options.
You can provide a dictionary of these options as `FROALA_EDITOR_OPTIONS` setting in `settings.py`. These options would then be used for all instances of the WYSIWYG editor in the project.

Options for individual field can also be provided via `FroalaField` or `FroalaEditor` class. This overrides any options set via `FROALA_EDITOR_OPTIONS`:

```python
from django.db import models
from froala_editor.fields import FroalaField

class Page(models.Model):
  content = FroalaField(options={
    'toolbarInline': True,
  })
```

```python
from django import forms
from froala_editor.widgets import FroalaEditor

class PageForm(forms.ModelForm):
  content = forms.TextField(widget=FroalaEditor(options={
    'toolbarInline': True,
  }))
```

### Theme

You may provide the name of the theme to be used as `theme` argument to `FroalaField` or `FroalaEditor`.

```python
from django.db import models
from froala_editor.fields import FroalaField

class Page(models.Model):
  content = FroalaField(theme='dark')
```

`FROALA_EDITOR_THEME` can be set in `settings.py` making all instances of the editor to use a theme. However, `theme` argument in `FroalaField` and `FroalaEditor` overrides `FROALA_EDITOR_THEME`. Using a theme named 'dark' would require the existence of the file `froala_editor/static/froala_editor/css/themes/dark.min.css`. Available themes are: 'dark', 'gray' and 'red'.

### Plugins

Froala Editor comes with the plugins: block style, text & background colors, font size, font family, insert video, insert table, media manager, lists and file upload. By default, all plugins are enabled by default in this package. See [https://froala.com/wysiwyg-editor/docs/plugins](<https://froala.com/wysiwyg-editor/docs/plugins>) for all available plugins.

`FROALA_EDITOR_PLUGINS` can be set in `settings.py` to tell which plugins should all instances of Froala Editor be using. By default, it is

```python
FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier' ,'code_view', 'colors', 'draggable', 'emoticons',
        'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image_manager', 'image', 'inline_style',
        'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert', 'quote', 'save', 'table',
        'url', 'video')
```

The usage of `plugins` argument with `FroalaEditor` or `FroalaField` overrides this for that particular instance.

```python
from django.db import models
from froala_editor.fields import FroalaField

class Page(models.Model):
  content = FroalaField(plugins=('font_size', 'font_family'))
```

### Third party integrations

`FROALA_EDITOR_THIRD_PARTY` setting can be used to configure third party integrations. Aviary Image Editor and SCAYT Web SpellChecker are available for now.
To enable, in `settings.py`:

```python
FRAOLA_EDITOR_THIRD_PARTY = ('image_aviary', 'spell_checker')
```

Similar to plugin configuration, this can also be overridden on `ForalaEditor` and `FroalaField`.

Use your key for SCAYT Web SpellChecker with `SCAYT_CUSTOMER_ID` in your project setings.


### Image upload

`FroalaEditor` and `FroalaField` optionally take in a boolean value for `image_upload` argument to enable or disable image uploads. Image uploads are enabled by default if the urls of this package are included in your urls.py.

You can use `FROALA_UPLOAD_PATH` setting in `settings.py` to change the path where uploaded files are stored within the `MEDIA_ROOT`. By default, `uploads/froala_editor/images` is used for storing uploaded images.

### Other Settings

`USE_FROALA_EDITOR` - default True  
 If set to Falsein your Django settings disables Froala editor and uses a TextArea instead.

`FROALA_STORAGE_BACKEND`  
This allows for the storage used for uploaded images and files to be changed through settings. If nothing is provided it uses default_storage, otherwise it uses this backend. Using this you can specify a different storage backend like S3 only for Froala.

`FROALA_JS_COOKIE` - default False.  
If set to True, it assumes [js-cookie](https://github.com/js-cookie/js-cookie) is installed and included to get the CSRF token using js-cookie.

### Release

To publish to PyPi, the following command should be run:
```bash
python setup.py sdist upload -r pypi
```

## License

This package is available under BSD License. However, in order to use Froala WYSIWYG HTML Editor plugin you should purchase a license for it.

See [https://froala.com/wysiwyg-editor/pricing](https://froala.com/wysiwyg-editor/pricing) for licensing the Froala Editor.

If you bought a license and got your key, the easiest way to implement it is to put it into the `FROALA_EDITOR_OPTIONS` setting in `settings.py`:

```python
FROALA_EDITOR_OPTIONS = {
  'key': '<our key goes here>',
  # other options
  # ...
}
