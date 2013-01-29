from distutils.core import setup

long_description = '''
marketo-python is a python query client that wraps the Marketo SOAP API.
For sending data to Marketo, check out https://segment.io.
'''

setup(
    name='marketo',
    version='0.0.3',
    url='https://github.com/segmentio/marketo-python',
    author='Ilya Volodarsky',
    author_email='ilya@segment.io',
    maintainer='Segment.io',
    maintainer_email='friends@segment.io',
    packages=['marketo', 'marketo.wrapper'],
    license='MIT License',
    install_requires=[
        'requests'
    ],
    description='marketo-python is a python query client that wraps the Marketo SOAP API.',
    long_description=long_description
)
