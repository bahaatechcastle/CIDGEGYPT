from odoo import models, fields, api


class container(models.Model):

    _name = 'container_num'

    name = fields.Char(string='name', tracking=True)
    total_bundle = fields.Integer(string="T Bundle", tracking=True)
    total_pallets = fields.Integer(string="T Pallets", tracking=True)
    total_box = fields.Integer(string="T Box", tracking=True)
    total_gw = fields.Float(string="T (GW)", tracking=True)
    total_nw = fields.Float(string="T (NW)", tracking=True)
    hs_code = fields.Char(string='HS Code', tracking=True)
    my_account_move_id_co = fields.Many2one('account.move', tracking=True)


class box_num(models.Model):

    _name = 'box_num'

    name = fields.Char(string='Number', tracking=True)
    product_ids = fields.Many2many('account.move.line', string='Products', tracking=True)
    my_account_move_id = fields.Many2one('account.move')
    container_num = fields.Many2one('container_num', string='Container Num', tracking=True)
    total_m2 = fields.Float(string='Total', compute='_total_price_', tracking=True)
    total_box = fields.Float(string='Total', compute='_total_box_', tracking=True)


    def _total_price_(self):
        for rec in self:
            rec.total_m2 = sum(rec.product_ids.mapped('quantity'))

    # def _total_box_(self):
    #     for rec in self:
    #         rec.total_m2 = sum(rec.product_ids.mapped('quantity'))



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
