======================
django-froala-editor
======================

django-froala-editor package helps integrate `Froala WYSIWYG editor <http://editor.froala.com/>`_ with Django.


Getting started
====================

1. Install the package::

    pip install git+git://github.com/xtranophilist/django-froala-editor.git

OR

Add the directory `froala_editor` from this repo to your Python path.

2. Add `froala_editor` to INSTALLED_APPS in `settings.py`.

Usage
==============
::

    from django.db import models
    from froala_editor.fields import FroalaField

    class Page(models.Model):
        content = FroalaField()

`FroalaField` uses `froala_editor.widgets.FroalaEditor` as its widget. You may directly use this widget with any of your forms.
::

    from django import forms
    from froala_editor.widgets import FroalaEditor

    class PageForm(forms.ModelForm):
        content = models.TextField(widget=FroalaEditor)


Options
==============

Froala Editor provides several options for customizing the editor. See http://editor.froala.com/docs for all available options.
You can provide a dictionary of these options as `FROALA_EDITOR_OPTIONS` setting in `settings.py`. These options would then be used for all instances of the WYSIWYG editor in the project.

Options for individual field can also be provided via FroalaField or FroalEditor class. This overrides any options set via `FROALA_EDITOR_OPTIONS`.::

    from django.db import models
    from froala_editor.fields import FroalaField

    class Page(models.Model):
        content = FroalaField(options={
            'inlineMode': True,
        })

::

    from django import forms
    from froala_editor.widgets import FroalaEditor

    class PageForm(forms.ModelForm):
        content = forms.TextField(widget=FroalaEditor(options={
            'inlineMode': True,
        }        ))

TO-DO
============
1. Make the editor work outside admin.
2. Support image and file upload.
3. Fix style
4. Upload to PyPI


License
===============

This package is licensed under WTFPL.
However, Froala editor is free only for non-commercial projects. For other uses, see http://editor.froala.com/download for licensing.