from odoo import models, fields, api


class code_product(models.Model):
    _inherit = "sale.order.line"

    item_code = fields.Char(string='Item Code', tracking=True)
    lenght = fields.Float(string='Lenght(MM)', tracking=True)
    width = fields.Float(string='Width(MM)', tracking=True)
    thickness = fields.Float(string='Thickness(MM)', tracking=True)
    no_of_tiles = fields.Integer(string='No. Of Tiles', tracking=True)
    container_num = fields.Many2one('container_num', string='Container Num')
    shape = fields.Char(string='Shape', tracking=True)
    surface = fields.Char(string='Surface', tracking=True)



    def _prepare_invoice_line(self, **optional_values):
        invoice_line = super()._prepare_invoice_line(**optional_values)
        invoice_line['container_num'] = self.container_num.id
        invoice_line['item_code'] = self.item_code
        invoice_line['lenght'] = self.lenght
        invoice_line['width'] = self.width
        invoice_line['thickness'] = self.thickness
        invoice_line['no_of_tiles'] = self.no_of_tiles
        invoice_line['quantity'] = self.product_uom_qty
        invoice_line['shape'] = self.shape
        invoice_line['surface'] = self.surface
        return invoice_line


    @api.onchange('lenght','width','no_of_tiles')
    def _area_calc(self):
        for rec in self:
            rec.product_uom_qty = rec.no_of_tiles * ((rec.width)/1000) * ((rec.lenght)/1000)