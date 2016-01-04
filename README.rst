# django-payline-dotir
use Iranian payment gateway  http://payline.ir in django (it's NOT related to payline.com).

====================
django-payline-dotir
====================

use payline_dotir to payment in http://payline.ir payment gatewary.
be aware that it's not related to payline.com. 

Detailed documentation is in the "docs" directory.

sample examle project is in the "example" directory.

Installation
------------
0. create a django project and payment app::
django-admin startproject payline_ir_proj
cd payline_ir_proj
django-admin startapp payment


1. install django-payline-dotir::
pip install django-payline-dotir

2. add "payment" to INSTALLED_APPS ::
    INSTALLED_APPS = (
        ...
        'payment',
    )

3. add PAYLINE_DOTIR_API = "your api key from http://payline.ir"
and for test purpose add IS_PAYLINE_DOTIR_TEST = True to settings.py

4. create your custom views, urls and templates.
example project is in the example directory.

5. Enjoy!

source code
-----------
source code can be found here

https://github.com/Bornazadeh/django-payline-dotir

Please use this repo for issue ,bug reporting and also patch and PR :).
