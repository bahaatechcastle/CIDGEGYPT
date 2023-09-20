from odoo import api, fields, models


class pos_category(models.Model):
    _inherit = "pos.category"

    order_line_ids = fields.One2many(comodel_name='pos.order.line', inverse_name='category_id', string='Orders',
                                     required=False, compute='_compute_orders')

    def _default_start_date(self):
        pos_sale = self.env['pos.order.line'].search([])
        return pos_sale[0].order_id.date_order or fields.Datetime.now()

    start_date = fields.Datetime(string='Start Date', required=False, default=_default_start_date)
    end_date = fields.Datetime(string='End Date', required=False)
    total_price = fields.Float(string='Total Price', required=False, compute='_compute_orders')
    total_discounts = fields.Float(string='Total Discounts', required=False, compute='_compute_orders')
    total_tax = fields.Float(string='Total Tax', required=False, compute='_compute_orders')
    total_without_tax = fields.Float(string='Total Without Tax', required=False, compute='_compute_orders')
    currency_id = fields.Many2one('res.currency', string="Currency", releted='user_id.currency_id')
    user_id = fields.Many2one(comodel_name='res.users', string='User_id', default=lambda self: self.env.user)

    @api.depends()
    def _compute_orders(self):
        for cate in self:
            print('currency_id', self.currency_id)
            print('user_id', self.user_id)
            pos_sale = self.env['pos.order.line'].search([('product_id.pos_categ_id', '=', cate.id)])
            cate.order_line_ids = pos_sale
            lines = []
            total = []
            discounts = []
            subtotal = []
            for line in pos_sale:
                if (cate.start_date and cate.end_date) and (
                        cate.end_date >= line.order_id.date_order >= cate.start_date):
                    lines.append(line.id)
                    total.append(line.price_subtotal_incl)
                    discounts.append(line.discount)
                    subtotal.append(line.price_subtotal)
            if len(lines) == 0:
                cate.order_line_ids = False
            else:
                cate.order_line_ids = lines
            cate.total_price = sum(total)
            cate.total_discounts = sum(discounts)
            cate.total_tax = (sum(total) - sum(subtotal)) + sum(discounts)
            cate.total_without_tax = sum(subtotal)
