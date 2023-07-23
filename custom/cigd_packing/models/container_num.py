from odoo import models, fields, api


class container(models.Model):

    _name = 'container_num'

    name = fields.Char(string='Name', tracking=True)
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
    no_of_tiles_con = fields.Float(string='No. Of Tiles', tracking=True)
    # total_amount = fields.Float(string='Total Amount', compute='_total_amount_', tracking=True)


    @api.constrains('container_num_id')
    def _on_change_box_no(self):
        for rec in self:
            rec.box_num = rec.env['box_num'].search(
                [('container_num', '=', rec.container_num_id.id), ('my_account_move_id', '=', rec.my_account_move_id_co._origin.id)])




    @api.constrains('container_num_id')
    def _total_m2_(self):
        for rec in self:
            # print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk,', rec.container_num_id.id)
            # print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk,', rec.my_account_move_id_co._origin.id)
            # print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk,', rec.box_num)
            total_m2 = []
            total_tiles = []
            for r in self.box_num:
                if rec.container_num_id._origin.id == r._origin.container_num._origin.id:
                    # print('lllllllllllllllllllllllllllllllll', r._origin.qty_box)
                    total_m2.append(float(r._origin.qty_box))
                    total_tiles.append(float(r._origin.no_of_tiles))
                    # print('lllllllllllllllllllllllllllllllll', r._origin.container_num._origin.name)
                    # print('ddddddddddddddddddddddddddddddddddddddddddddddddd',total)
                    print('ddddddddddddddddddddddddddddddddddddddddddddddddd',total_tiles)
            rec.total_m2_con = sum(total_m2)
            rec.no_of_tiles_con = sum(total_tiles)
            # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',rec.total_m2_con)



    @api.depends()
    def _total_box(self):
        for rec in self:
            rec.total_box = len(rec.box_num.mapped('box_num_id'))

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


