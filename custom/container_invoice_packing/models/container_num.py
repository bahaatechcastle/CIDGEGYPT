from odoo import models, fields, api


class container(models.Model):

    _name = 'container_num'

    name = fields.Char(string='name', tracking=True)
    container_num_id = fields.Many2one('container_num', string='Name', tracking=True)
    total_bundle = fields.Integer(string="T Bundle", tracking=True)
    total_pallets = fields.Integer(string="T Pallets", tracking=True)
    total_box = fields.Integer(string="T Box", tracking=True, compute='_total_box',)
    total_gw = fields.Float(string="T (GW)", tracking=True)
    total_nw = fields.Float(string="T (NW)", tracking=True)
    hs_code = fields.Char(string='HS Code', tracking=True)
    my_account_move_id_co = fields.Many2one('account.move', tracking=True)
    box_num = fields.One2many('box_num', 'container_num', string='Box No.', tracking=True, compute='_on_change_box_no')
    total_m2_con = fields.Float(string='Total', compute='_total_m2_', tracking=True)
    invoice_name = fields.Char(string='Invoice Name', releted='my_account_move_id_co.name', tracking=True)
    # total_amount = fields.Float(string='Total Amount', compute='_total_amount_', tracking=True)


    @api.constrains('container_num_id')
    def _on_change_box_no(self):
        for rec in self:
            rec.box_num = rec.env['box_num'].search(
                [('container_num', '=', rec.container_num_id._origin.id), ('my_account_move_id', '=', rec.my_account_move_id_co._origin.id)])
            print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk,',rec.container_num_id._origin.id)
            print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk,',rec.box_num)
            for r in self.box_num:
                print('lllllllllllllllllllllllllllllllll',r._origin.name)
                print('lllllllllllllllllllllllllllllllll',r._origin.container_num._origin.name)

    def _total_m2_(self):
        for rec in self:
            rec.total_m2_con = sum(rec.box_num.mapped('total_m2_box'))

    @api.depends()
    def _total_box(self):
        for rec in self:
            rec.total_box = len(rec.box_num.mapped('name'))

    # @api.depends()
    # def _total_amount_(self):
    #     for rec in self:
    #         rec.total_box = sum(rec.box_num.mapped('total_amount'))


    # @api.constrains('box_num', 'invoice_name')
    # def _create_box(self):
    #     for rec in self:
    #
    #         y = {'container_num': rec.name,
    #              'invoice_name': rec.invoice_name,
    #              'name': rec.box_num.name,
    #              }
    #
    #         x = self.env['box_num'].create(y)
    #         print('kkkkkkkkkkkkkkkkkkkkk', x.box_num.name)


class box_num(models.Model):

    _name = 'box_num'

    name = fields.Char(string='Number', tracking=True)
    box_num_id = fields.Many2one('box_num', string='Number', tracking=True)
    product_ids = fields.Many2many('account.move.line', string='Products', tracking=True)
    my_account_move_id = fields.Many2one('account.move', tracking=True)
    container_num = fields.Many2one('container_num', string='Container Num', tracking=True)
    total_m2_box = fields.Float(string='Total', compute='_total_price_', tracking=True)
    total_box = fields.Float(string='Total', compute='_total_box_', tracking=True)
    total_amount = fields.Float(string='Total', compute='_total_amount_', tracking=True)
    invoice_name = fields.Char(string='Invoice Name', tracking=True)


    def _total_price_(self):
        for rec in self:
            rec.total_m2_box = sum(rec.product_ids.mapped('quantity'))


    @api.depends()
    def _total_amount_(self):
        for rec in self:
            rec.total_amount = sum(rec.product_ids.mapped('price_subtotal'))

    # def _total_box_(self):
    #     for rec in self:
    #         rec.total_m2 = sum(rec.product_ids.mapped('quantity'))

    @api.onchange('box_num_id', 'container_num')
    def _on_change_box_no(self):
        self.product_ids = self.env['account.move.line'].search(
            [('container_num', '=', self.container_num._origin.id),('move_id', '=', self.my_account_move_id._origin.id)])
        for r in self.product_ids:
            print('lllllllllllllllllllllllllllllllll', r._origin.name)
            print('lllllllllllllllllllllllllllllllll', r._origin.container_num._origin.name)






    # @api.depends()
    # def _compute_product(self):
    #     for rec in self:
    #         product = rec.env['account.move.line'].search([('id', '=', self.id)]).

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.optional_id = False
            optional_products = self.product_id.optional_product_ids.ids
            if optional_products:
                domain = [('id', 'in', optional_products)]
                return {'domain': {'optional_id': domain}}
        return {'domain': {'optional_id': [('id', 'in', [])]}}
