# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2018 Odoo Helper
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Website Product Quantity',
    'category': 'Website',
    'summary': "Website Product Quantity Module",

    'version': '13.0.1',
    'description': """
Website Product Quantity
==================
If customer dosen't need to 1 kg than we provide 1/4, 1/2 and 3/4 kg so customer easily buy.
        """,

    'author': 'Odoo Helper',
    'depends': ['website_sale'],
    'data': [
        'views/assets.xml',
        'views/template.xml',
    ],
    'images': ['images/OdooHelper.jpg'],
    'price': 11.41,
    'currency': 'USD',

    'application': True,
    'installable': True,
    'auto_install': False,
}

