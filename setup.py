from distutils.core import setup

setup(
    name='DjangoFroalaEditor',
    version='0.6.0',
    author='Dipesh Acharya',
    author_email='xtranophilist@gmail.com',
    packages=['froala_editor'],
    url='http://github.com/xtranophilist/django-froala-editor/',
    license='MIT',
    description='django-froala-editor package helps integrate Froala WYSIWYG editor  with Django.',
    long_description=open('README.txt').read(),
    include_package_data=True,
    zip_safe=False,
    keywords='froala,django,admin,wysiwyg,editor',
)