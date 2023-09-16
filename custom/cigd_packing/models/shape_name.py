from odoo import fields, models, api


class ShapeName(models.Model):
    _name = 'shape.name'

    name = fields.Char()
