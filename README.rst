# django-payline-dotir
use Iranian payment gateway  http://payline.ir in django (it's NOT related to payline.com).

====================
django-payline-dotir
====================

use payline_dotir to payment in http://payline.ir payment gatewary.
be aware tha it's not related to payline.com. 

Detailed documentation is in the "docs" directory.

Installation
------------
0. create a django project
django-admin startproject payline_ir

1. install django-payline-dotir
pip install django-payline-dotir

2. add "payline_dotir" to INSTALLED_APPS ::
    INSTALLED_APPS = (
        ...
        'payline_dotir',
    )

3. add PAYLINE_DOTIR_API = "your api key from http://payline.ir"
and for test ourpese add IS_PAYLINE_DOTIR_TEST = True to settings.py

4. Run `python manage.py migrate` to create the polls models.

