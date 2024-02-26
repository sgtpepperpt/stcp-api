from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='stcp_api',
    version='1.1.1',
    author='Guilherme Borges',
    author_email='g@guilhermeborges.net',
    description='Unofficial API to retrieve STCP information for public transit buses in Porto, Portugal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sgtpepperpt/stcp-api',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'urllib3'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
