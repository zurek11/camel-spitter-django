from setuptools import setup


def read_files(files):
    data = []
    for file in files:
        with open(file) as f:
            data.append(f.read())
    return "\n".join(data)


meta = {}
with open('./camel_spitter/version.py') as f:
    exec(f.read(), meta)

setup(
    name='django-camel-spitter',
    version=meta['__version__'],
    packages=[
        'camel_spitter'
    ],
    install_requires=[
        'Django>=2.0'
    ],
    url='https://github.com/zurek11/django-camel-spitter',
    license='MIT',
    author='Adam Žúrek',
    author_email='adamzurek14@gmail.com',
    description='A library which add DBHandler to Django logging handlers.',
    long_description=read_files(['README.md', 'CHANGELOG.md']),
    long_description_content_type='text/markdown',
    classifiers=[
        # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
    ]
)
