# -*- coding: utf-8 -*-
{
    'name': "Visit Customer POS",

    'summary': """
        number time visit customer pos""",

    'description': """
       number time visit customer pos
    """,

    'author': "Tech Castle",
    'website': "https://techcastle.net/",

    'category': 'Point of sale',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'point_of_sale'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/visit_customer_pos.xml',
        'views/res_partner.xml',
        'wizard/visit_pos_date.xml',
        'report/reports.xml',
        'report/report_visit_customer_pos.xml',
    ],
}
