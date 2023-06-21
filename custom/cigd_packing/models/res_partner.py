from odoo import models, fields, api


class codePartner(models.Model):
    _inherit = "res.partner"

    code = fields.Char(string='Code')