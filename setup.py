from setuptools import setup, find_packages

setup(
    name='medium-article-py',
    version='v0.1',
    description='A simple python library for Medium Articles APIs',
    author='Your Name',
    author_email='umuhammad202@yahoo.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
    download_url='https://github.com/muhammad-usman-108/medium-article-py.git',
    keywords=['medium', 'medium-api', 'medium-article', 'api']
)