

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    text_test = fields.Char(string='test')
    email_parent = fields.Char(string='Email Parent', default=False, )
    phone_whatsapp = fields.Char(string='Phone Whatsapp', default=False, )
    phone_2 = fields.Char(string='Phone 2', default=False, )
    profession = fields.Char(string='Profession', default=False, )
    note = fields.Text(string='Note', default=False, )
    parent_name = fields.Char(string='Parent Name')
    # source_id = fields.Many2one('utm.source', string='Source')
    source = fields.Char(string='Source')
    birthday_kid = fields.Date(string='Kid Birthday', required=False)
    age = fields.Integer(string='Kid Age', required=False)
