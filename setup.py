import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-payline-dotir',
    version='0.2',
    author='Mahdi Bornazadeh',
    author_email='Bornazadeh@gmail.com',
    description='Persian payline.ir payment gateway in django.',
    long_description=open("README.rst", 'rb').read().decode('utf-8'),
    license='BSD License',
    url='http://www.bornazadeh.ir/payline',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),

    install_requires=[
        "requests",
    ],

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: "
        "Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
