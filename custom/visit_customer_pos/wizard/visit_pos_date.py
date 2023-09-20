from odoo import fields, models, api


class pos_sale_category(models.TransientModel):
    _name = 'visit.pos.date'

    start_data = fields.Datetime(string='Start Data', required=False,
                                 default=lambda s: s.env['pos.order'].search([])[0].date_order)
    end_data = fields.Datetime(string='End Data', required=False, default=fields.Datetime.now)

    def action_open_visit_pos_data(self):
        visit_date = self.env['visit.customer.pos'].search([])[-1]
        print('visit_date', visit_date)
        w = visit_date.write({
            'start_date': self.start_data,
            'end_date': self.end_data
        })
        print('wwwwwwwwwwwwwwwwwwwww', w)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Visit POS',
            'res_model': 'visit.customer.pos',
            'view_mode': 'tree',
            'domain': [('customer', '=', visit_date.customer.id), ('start_date', '=', self.start_data),
                       ('end_date', '=', self.end_data), ('id', '=', visit_date.id), ],
            'target': 'current',
        }
