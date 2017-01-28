from setuptools import setup

README = os.path.join(os.path.dirname(__file__), 'README.rst')

try:
    with open(README) as file:
        long_description = file.read()
except Exception:
    long_description = ''


setup(
    name='django-froala-editor',
    version='2.4.1',
    author='Dipesh Acharya',
    author_email='xtranophilist@gmail.com',
    maintainer='Froala Labs',
    maintainer_email='stefan@froala.com',
    packages=['froala_editor'],
    url='http://github.com/froala/django-froala-editor/',
    license='BSD License',
    description='django-froala-editor package helps integrate Froala WYSIWYG HTML editor with Django.',
    long_description=long_description,
    include_package_data=True,
    zip_safe=False,
    keywords='froala,django,admin,wysiwyg,editor,text,html,editor,rich, web',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
