from odoo import models, fields, api

class box_num(models.Model):

    _name = 'box_num'

    name = fields.Char(string='Number', tracking=True)
    box_num_id = fields.Many2one('box_num', string='Number', tracking=True)
    # product_ids = fields.Many2many('sale.order.line', string='Products', tracking=True)
    product_id = fields.Many2one('sale.order.line', string='Product', tracking=True )
    my_account_move_id = fields.Many2one('account.move', tracking=True)
    container_num = fields.Many2one('container_num', string='Container Num', tracking=True)
    total_m2_box = fields.Float(string='Total',related='product_id.product_uom_qty', tracking=True)
    # total_box = fields.Float(string='Total', compute='_total_box_', tracking=True)
    # total_amount = fields.Float(string='Total', related='product.', tracking=True)
    invoice_name = fields.Char(string='Invoice Name', tracking=True)
    packing_id_box = fields.Many2one('stock.picking', tracking=True)
    packing_id_box_invoice = fields.Many2one('stock.picking', tracking=True)
    sale_name = fields.Char(related='packing_id_box.origin', tracking=True)
    qty_box = fields.Char(string='Qty for Box', tracking=True, compute='_total_area_')
    no_of_tiles = fields.Float(string='No. Of Tiles', tracking=True)
    dis_product = fields.Text(string='Dis Product', related='product_id.name')



    def _total_price_(self):
        for rec in self:
            rec.total_m2_box = sum(rec.product_ids.mapped('quantity'))


    @api.depends()
    def _total_amount_(self):
        for rec in self:
            rec.total_amount = sum(rec.product_ids.mapped('price_subtotal'))

    @api.onchange('no_of_tiles')
    def _total_area_(self):
        for rec in self:
            rec.qty_box = ((rec.product_id.width)/1000) * ((rec.product_id.lenght)/1000) * rec.no_of_tiles



    # @api.onchange('box_num_id', 'container_num')
    # def _on_change_box_no(self):
    #     if self.container_num:
    #         self.product_ids = self.env['sale.order.line'].search(
    #             [('container_num', '=', self.container_num._origin.id),('sale_id', '=', self.product_ids._origin.id)])
    #         for r in self.product_ids:
    #             print('lllllllllllllllllllllllllllllllll', r._origin.name)
    #             print('lllllllllllllllllllllllllllllllll', r._origin.container_num._origin.name)






