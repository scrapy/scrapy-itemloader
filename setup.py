from setuptools import setup

setup(
    name='scrapy-itemloader',
    version='0.1.0',
    license='BSD',
    description='Library to populate Scrapy items with a convenient API',
    author='Scrapinghub',
    author_email='info@scrapinghub.com',
    url='https://github.com/scrapy/scrapy-itemloader',
    packages=['scrapy_itemloader'],
    platforms=['Any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=['scrapy', 'six']
)
