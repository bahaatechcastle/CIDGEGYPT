# -*- coding: utf-8 -*-
{
    'name': "POS Customers",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [
        'point_of_sale',
        'contacts',
        'base',
        'utm',
    ],

    'data': [
        'views/views.xml',
    ],
    'assets': {
		'point_of_sale.assets': [
            'pos_customers_add/static/src/js/models.js',
        ],
        'web.assets_qweb': [
                'pos_customers_add/static/src/xml/Screens/ClientListScreen/ClientDetailsEdit.xml',
        ]
    }

}
