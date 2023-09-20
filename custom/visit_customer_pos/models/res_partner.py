# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_open_visit_pos_data(self):
        unlink = self.env['visit.customer.pos'].search([]).unlink()
        print('unlink', unlink)
        visit_pos = self.env['visit.customer.pos'].create({
            'customer': self.id
        })
        print('visit_pos', visit_pos)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Visit POS',
            'res_model': 'visit.pos.date',
            'view_mode': 'form',
            'target': 'new',
            'context': {'create': False, 'delete': False, 'edit': False},
        }
