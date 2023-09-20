{
    'name': 'Sale By Category Report',
    'version': '16.0.0',
    'summary': 'Report to Category ',
    'category': 'Point of sale',

    'author': "Tech Castle",
    'website': "https://techcastle.net/",

    'depends': [
        'base',
        'point_of_sale',
    ],

    'data': [
        'security/ir.model.access.csv',
        'wizard/pos_salecategory.xml',
        'views/pos_category.xml',
        'report/reports.xml',
        'report/report_salecategory.xml',
    ],

    'installable': True,
    'auto_install': False
}
