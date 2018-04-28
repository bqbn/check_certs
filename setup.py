"""
For references of this file, see

https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='check_certs',
    version='0.1.3',
    description='''Check TLS certificates of sites for their expiration
                   dates. Send notifications if configured to do so.''',

    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/bqbn/check_certs',
    author='bqbn',
    author_email='bqbn@openken.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='ssl tls tools development devops',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'boto3',
        'botocore',
        'cryptography',
        'pluginbase',
        'PyYAML',
    ],

    extras_require={
        'dev': [],
        'test': [],
    },

    entry_points={
        'console_scripts': [
            'check_certs=check_certs.check_certs:main',
        ],
    },

    project_urls={
        'Bug Reports': 'https://github.com/bqbn/check_certs/issues',
        'Source': 'https://github.com/bqbn/check_certs',
    },
)

