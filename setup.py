from setuptools import setup

setup(
    name='django-froala-editor',
    version='1.2.3.1',
    author='Dipesh Acharya',
    author_email='xtranophilist@gmail.com',
    packages=['froala_editor'],
    url='http://github.com/froala/django-froala-editor/',
    license='BSD License',
    description='django-froala-editor package helps integrate Froala WYSIWYG editor with Django.',
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False,
    keywords='froala,django,admin,wysiwyg,editor,text,html,editor',
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
