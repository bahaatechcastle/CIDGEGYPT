from odoo import fields, models, api



class pos_sale_category(models.TransientModel):
    _name = 'pos_sale_category_report'

    start_data = fields.Datetime(string='Start Data', required=False,
                                 default=lambda s: s.env['pos.order.line'].search([])[0].order_id.date_order)
    end_data = fields.Datetime(string='End Data', required=False, default=fields.Datetime.now)
    order_line_ids = fields.One2many(comodel_name='pos.order.line', inverse_name='category_id', string='Orders',
                                     required=False, compute='_compute_orders')
    pos_category_ids = fields.Many2many(comodel_name='pos.category', string='Pos_category_ids'
                                        , default=lambda s: s.env['pos.category'].search([]))

    # @api.onchange('start_data')
    # def _compute_orders(self):
    #     pos_category = self.env['pos.category'].search([])
    #     if pos_category.order_line_ids:
    #         self.pos_category_ids = pos_category
    #         for cate in pos_category:
    #             w = cate.write({
    #                 'start_date': self.start_data,
    #                 'end_date': self.end_data
    #             })
    #             print('wwwwwwwwwwwwwwwwwwwww', w)
    #             self.order_line_ids = pos_category.order_line_ids

    def generate_report(self):
        pos_category = self.env['pos.category'].search([])
        self.pos_category_ids = pos_category
        for cate in pos_category:
            w = cate.write({
                'start_date': self.start_data,
                'end_date': self.end_data
            })
            print('wwwwwwwwwwwwwwwwwwwww', w)
            self.order_line_ids = pos_category.order_line_ids
        return {
            'type': 'ir.actions.act_window',
            'name': 'Category',
            'res_model': 'pos.category',
            'view_mode': 'tree,form',
            'target': 'current',
        }
        #         {
        #     'type': 'ir.actions.client',
        #     'tag': 'reload',
        # }
