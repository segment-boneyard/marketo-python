
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Don't import analytics-python module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'marketo'))
from version import VERSION

long_description = '''
marketo-python is a python query client that wraps the Marketo SOAP API.
For sending data to Marketo, check out https://segment.io.
'''

setup(
    name='marketo',
    version=VERSION,
    url='https://github.com/segmentio/marketo-python',
    author='Ilya Volodarsky',
    author_email='ilya@segment.io',
    maintainer='Segment.io',
    maintainer_email='friends@segment.io',
    packages=['marketo', 'marketo.wrapper'],
    license='MIT License',
    install_requires=[
        'requests',
        'iso8601'
    ],
    description='marketo-python is a python query client that wraps the Marketo SOAP API.',
    long_description=long_description
)
