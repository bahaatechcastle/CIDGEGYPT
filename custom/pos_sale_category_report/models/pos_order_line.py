from odoo import fields, models, api


class pos_order_line(models.Model):
    _inherit = 'pos.order.line'

    category_id = fields.Many2one(
        comodel_name='pos.category',
        string=' Category',
        required=False)



