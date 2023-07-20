# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    company_id = fields.Many2one(default=lambda self: self.env.company)

