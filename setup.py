import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='medium-article-py',
    version='v0.1.6',
    description='A simple python library for Medium Articles APIs',
    long_description=long_description,
    author='Muhammad Usman',
    author_email='umuhammad202@yahoo.com',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
    download_url='https://github.com/muhammad-usman-108/medium-article-py.git',
    keywords=['medium', 'medium-api', 'medium-article', 'api'],
)