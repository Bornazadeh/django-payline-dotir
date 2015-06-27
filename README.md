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
1. install django-payline-dotir
pip install django-payline-dotir

2. add "payline_dotir" to INSTALLED_APPS ::
    INSTALLED_APPS = (
        ...
        'payline_dotir',
    )

3. Include the polls URLconf in your project urls.py like this::

    url(r'^payline_dotir', include('payline_dotir.urls')),

4. Run `python manage.py migrate` to create the polls models.

