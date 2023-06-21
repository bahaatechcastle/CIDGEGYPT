# -*- coding: utf-8 -*-
{
    'name': "cidg_packing_manf",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'account',
                'sale',
                'mrp',
                ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'report/invoice_container_2_report.xml',
        'report/invoice_container_report.xml',
        'report/packing_container_report.xml',
        'views/inherit_packing_report.xml',
        'views/inherit_manf_report.xml',
        'views/account_move.xml',
        'views/res_bank.xml',
        'views/sale_order.xml',
        'views/mrp_production.xml',
        'views/stock_picking.xml',
        # 'views/container_num.xml',
    ],

}
