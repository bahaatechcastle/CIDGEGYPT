# -*- coding: utf-8 -*-

from odoo import models, fields


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_partner(self):
        result = super()._loader_params_res_partner()
        result['search_params']['fields'].append('email_parent')
        result['search_params']['fields'].append('phone_whatsapp')
        result['search_params']['fields'].append('phone_2')
        result['search_params']['fields'].append('profession')
        result['search_params']['fields'].append('note')
        result['search_params']['fields'].append('parent_name')
        # result['search_params']['fields'].append('source')
        result['search_params']['fields'].append('birthday_kid')
        return result
