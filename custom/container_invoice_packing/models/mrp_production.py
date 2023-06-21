from odoo import models, fields, api


class mo_new(models.Model):
    _inherit = 'mrp.production'

    item_code = fields.Char(string='Item Code', tracking=True)
    lenght = fields.Float(string='Lenght(MM)', tracking=True)
    width = fields.Float(string='Width(MM)', tracking=True)
    thickness = fields.Float(string='Thickness(MM)', tracking=True)
    no_of_tiles = fields.Float(string='No. Of Tiles', tracking=True)
    container_num = fields.Many2one('container_num', string='Container Num', tracking=True)
    shape = fields.Char(string='Shape', tracking=True)
    surface = fields.Char(string='Surface', tracking=True)
    order_id = fields.Many2one('sale.order', string='Order', tracking=True)
    sale = fields.Char(string='Order', related='order_id.name', tracking=True)
    order_partner_id = fields.Many2one('res.partner', string='partner', tracking=True)
    code_partner = fields.Char(string='partner Code', related='order_partner_id.code', tracking=True)
