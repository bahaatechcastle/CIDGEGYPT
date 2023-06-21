from odoo import models, fields, api


class mobilebank(models.Model):
    _inherit = "res.bank"

    mobile = fields.Char(string="Mobile", tracking=True)
    country_id = fields.Many2one("res.country", tracking=True)
    website = fields.Char(string="Website", tracking=True)
    vat = fields.Char(string="Vat", tracking=True)
    swift_code = fields.Char(string='Swift Code', tracking=True)
    branch = fields.Char(string='Branch', tracking=True)
    usd_iban = fields.Char(string='USD IBAN', tracking=True)
