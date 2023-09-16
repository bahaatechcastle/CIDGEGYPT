from odoo import models, fields, api


class code_product(models.Model):
    _inherit = "account.move.line"

    item_code = fields.Char(string='Item Code', tracking=True, )
    lenght = fields.Float(string='Lenght(MM)', tracking=True)
    width = fields.Float(string='Width(MM)', tracking=True)
    thickness = fields.Float(string='Thickness(MM)', tracking=True)
    no_of_tiles = fields.Integer(string='No. Of Tiles', tracking=True)
    container_num = fields.Many2one('container_num', string='Container Num', tracking=True)
    # shape = fields.Char(string='Shape', tracking=True)
    shape = fields.Many2one(comodel_name='shape.name', string='Shape', required=False)
    surface = fields.Char(string='Surface', tracking=True)
