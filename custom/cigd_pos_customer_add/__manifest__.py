# -*- coding: utf-8 -*-

{
    'name': 'Customer Add In POS To CIGD',
    'version': '16',

    'category': 'Point of Sale',
    'author': "TechCastle",
    'website': "https://techcastle.net/",
    'depends': [
        'base',
        'point_of_sale',
        'utm'
    ],
    'data': [
        'views/res_partner.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'cigd_pos_customer_add/static/src/js/Screens.js',
            'cigd_pos_customer_add/static/src/xml/**/*',

        ],
    },

    'application': False,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
