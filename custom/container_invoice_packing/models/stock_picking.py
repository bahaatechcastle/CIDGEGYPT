from odoo import models, fields, api




class packing_new(models.Model):
    _inherit = 'stock.picking'

    my_sale_order_ids = fields.One2many('sale.order.line', 'packing_id', string='Sale Line', tracking=True)
    box_num = fields.One2many('box_num', 'packing_id_box', string='Box Number' , tracking=True)
    box_num_invoice = fields.One2many('box_num', 'packing_id_box_invoice', string='Box Number Invoice' , tracking=True)
    box = fields.Boolean(string='Box', tracking=True)
    pa_in_id = fields.Many2one('stock.picking')
    pa_in_ids = fields.One2many('stock.picking', 'pa_in_id', string='pa invoice')
    product_ids = fields.One2many('sale.order.line', 'box_num_in', string='product')
    num_box = fields.Many2one('box_num', string='Number Box')
    container_num = fields.Many2one('container_num')
    code_partner = fields.Char(string='partner Code', related='partner_id.code', tracking=True)


    @api.onchange('box')
    def _sale_id(self):
        for rec in self:
            rec.my_sale_order_ids = rec.env['sale.order'].search(
                [('name', '=', rec.origin)]).order_line
            print('ffffffffffffffffffffffff',rec.my_sale_order_ids)



    # @api.onchange('origin')
    # def _mapped_product(self):
    #
    #     for line in self:
    #         x = line.box_num.mapped('box_num_id')
    #         for pro in x:
    #             line.num_box = pro
    #             print('ppppppppppppppppppppppppppppppppppp',pro)
    #             # print('ppppppppppppppppppppppppppppppppppp',pro.name)
    #             for rec in line.box_num:
    #                 if pro.id == rec._origin.box_num_id.id:
    #                     line.product_ids = rec._origin.product_id
    #                     # print('ddddddddddddddddddddddddddddd',rec._origin.box_num_id.id)
    #                     print('ddddddddddddddddddddddddddddd',rec._origin.product_id.product_template_id)


