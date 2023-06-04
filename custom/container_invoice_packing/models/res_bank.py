from odoo import models, fields, api


class mobilebank(models.Model):
    _inherit = "res.bank"

    mobile = fields.Char(string="Mobile")
    country_id = fields.Many2one("res.country")
    website = fields.Char(string="Website")
    vat = fields.Char(string="Vat")
    swift_code = fields.Char(string='Swift Code')
    branch = fields.Char(string='Branch')
    usd_iban = fields.Char(string='USD IBAN')
