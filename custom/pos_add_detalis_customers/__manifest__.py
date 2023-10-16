{
    'name': 'Add Details in customer',
    'version': '16.1.0.0',
    'summary': 'Add Details in customer',
    'category': 'point of sale',
    'author': "Tech Castle",
    'website': "https://techcastle.net/",
    'license': 'LGPL-3',
    'depends': [
        'base',
        'point_of_sale',
    ],
    'data': [
        'views/res_partner.xml',
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_add_detalis_customer/static/src/xml/PartnerDetailsEdit.xml",
            "pos_add_detalis_customer/static/src/js/PartnerDetailsEdit.js",
        ],

    },
    'installable': True,
    'auto_install': False
}
