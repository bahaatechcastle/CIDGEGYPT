# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date


class VisitCustomerPOS(models.Model):
    _name = 'visit.customer.pos'

    customer = fields.Many2one(comodel_name='res.partner', string='Customer', required=False,
                               domain="[('pos_order_ids', '!=', False)]")
    pos_order_ids = fields.One2many(comodel_name='pos.order', inverse_name='visit_customer_id', string='POS Orders',
                                    required=False, compute='_compute_pos_orders')
    start_date = fields.Datetime(string='Start Date', required=False,
                                 default=lambda s: s.env['pos.order'].search([])[-1].date_order)
    end_date = fields.Datetime(string='End Date', required=False,
                               default=lambda s: s.env['pos.order'].search([])[0].date_order)
    count_pos_orders = fields.Integer(string='Count POS Orders', required=False, compute='_compute_pos_orders')
    count_visit = fields.Integer(string='Count Visit', required=False, compute='_compute_pos_orders')

    #
    @api.depends('customer', 'start_date', 'end_date')
    def _compute_pos_orders(self):
        for visit in self:
            pos_orders = self.env['pos.order'].search(
                [('partner_id', '=', visit.customer.id), ('date_order', '>=', visit.start_date),
                 ('date_order', '<=', visit.end_date)])
            count_pos_orders = self.env['pos.order'].search_count(
                [('partner_id', '=', visit.customer.id), ('date_order', '>=', visit.start_date),
                 ('date_order', '<=', visit.end_date)])
            print('pos_orders', pos_orders)
            visit.pos_order_ids = pos_orders
            visit.count_pos_orders = count_pos_orders
            datas = []
            for order in pos_orders:
                if datetime.date(order.date_order) in datas:
                    pass
                else:
                    datas.append(datetime.date(order.date_order))
                print('date', datetime.date(order.date_order))
                print('datas', datas)
            visit.count_visit = len(datas)




