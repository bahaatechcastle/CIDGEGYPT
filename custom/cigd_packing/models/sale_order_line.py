from odoo import models, fields, api
from datetime import timedelta


class code_product(models.Model):
    _inherit = "sale.order.line"

    item_code = fields.Char(string='Item Code', tracking=True)
    lenght = fields.Float(string='Lenght(MM)', tracking=True)
    width = fields.Float(string='Width(MM)', tracking=True)
    thickness = fields.Float(string='Thickness(MM)', tracking=True)
    no_of_tiles = fields.Float(string='No. Of Tiles', tracking=True)
    container_num = fields.Many2one('container_num', string='Container Num', tracking=True)
    # shape = fields.Char(string='Shape', tracking=True)
    shape = fields.Many2one(comodel_name='shape.name', string='Shape', required=False)
    surface = fields.Char(string='Surface', tracking=True)
    packing_id = fields.Many2one('stock.picking', tracking=True)
    box_num = fields.Many2one('box_num', string='Box Num', tracking=True)
    box_num_in = fields.Many2one('box_num', string='Box Num', tracking=True)

    def _prepare_invoice_line(self, **optional_values):
        invoice_line = super()._prepare_invoice_line(**optional_values)
        invoice_line['container_num'] = self.container_num.id
        invoice_line['item_code'] = self.item_code
        invoice_line['lenght'] = self.lenght
        invoice_line['width'] = self.width
        invoice_line['thickness'] = self.thickness
        invoice_line['no_of_tiles'] = self.no_of_tiles
        invoice_line['quantity'] = self.product_uom_qty
        invoice_line['shape'] = self.shape.id
        invoice_line['surface'] = self.surface
        return invoice_line

    @api.onchange('lenght', 'width', 'product_uom_qty')
    def _area_calc(self):
        if self.width != 0 and self.lenght != 0:
            for rec in self:
                rec.no_of_tiles = rec.product_uom_qty / (((rec.width) / 1000) * ((rec.lenght) / 1000))

    # @api.onchange('no_of_tiles')
    # def _area_calc(self):
    #     if self.no_of_tiles != 0 :
    #         for rec in self:
    #             rec.product_uom_qty = rec.no_of_tiles * (((rec.width)/1000) * ((rec.lenght)/1000))


class sale(models.Model):
    _inherit = "sale.order"

    mo = fields.Boolean(string='Mo')

    @api.onchange('mo')
    def _on_change_product(self):
        for rec in self:
            x = rec.order_line
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', x)
            for line in x:
                y = {'item_code': line.item_code,
                     'product_id': line.product_id.id,
                     'order_partner_id': line.order_partner_id.id,
                     'order_id': line.order_id.id,
                     'lenght': line.lenght,
                     'width': line.width,
                     'thickness': line.thickness,
                     'no_of_tiles': line.no_of_tiles,
                     'shape': line.shape.id,
                     'surface': line.surface,
                     'product_qty': line.product_uom_qty,
                     }
                z = self.env['mrp.production'].create(y)
                print('gggggggggggggggggggggggggggggggggg', z)
