{
    'name': 'Add Details in customers',
    'version': '16.1.0.1',
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
            "pos_add_detalis_customers/static/src/xml/PartnerDetailsEdit.xml",
            "pos_add_detalis_customers/static/src/js/PartnerDetailsEdit.js",
        ],

    },

}
