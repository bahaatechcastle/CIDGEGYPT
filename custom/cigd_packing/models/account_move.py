from odoo import models, fields, api


class ShippingData(models.Model):
    _inherit = "account.move"

    Container_no = fields.Integer(string="Container NO.", tracking=True,  compute='_total_container_',)
    box_no = fields.Integer(string="Box NO.", tracking=True,  compute='_total_box_',)
    container_num = fields.One2many('container_num', 'my_account_move_id_co', string='Container Number' , tracking=True)
    box_num = fields.One2many('box_num', 'my_account_move_id', string='Box Number' , tracking=True)
    bl_num = fields.Char(string="B/L NO.", tracking=True)
    total_bundle = fields.Integer(string="Total Bundle", tracking=True,  compute='_total_total_bundle_',)
    total_pallets = fields.Integer(string="Total Pallets", tracking=True,  compute='_total_total_pallets_',)
    total_box = fields.Integer(string="Total Box", tracking=True)
    total_gw = fields.Float(string="Total (GW)", tracking=True, compute="_total_total_gw_")
    total_nw = fields.Float(string="Total (NW)", tracking=True, compute="_total_total_nw_")
    bank_details = fields.Many2one('res.bank', string='BANK DETAILS', tracking=True, related='account_number.bank_id')
    account_num = fields.Char(string='Account Number', tracking=True)
    account_number = fields.Many2one('res.partner.bank', string='Account Number', tracking=True)
    shipping = fields.Boolean(string='Shipping Invoice', tracking=True)
    packing = fields.Boolean(string='Packing Container', tracking=True)
    total_m2 = fields.Float(string='Total', compute='_total_price_', tracking=True)
    # total_amount = fields.Float(string='Total Amount', compute='_total_amount_', tracking=True)
    sale_order_num = fields.Char(string='Quotation NO.', compute="_compute_sale_order_name", tracking=True)
    po_num = fields.Char(string='PO NO.', tracking=True)
    po_destination = fields.Char(string='Port OF Destination', tracking=True)
    terms_of_payment = fields.Char(string='Terms of payment:', tracking=True)
    the_prices_are = fields.Char(string='The prices are:', tracking=True)
    port_of_loading = fields.Char(string='Port of Loading:', tracking=True)
    ship_date = fields.Date(string='Ship Date', tracking=True)
    ship_via = fields.Char(string='Ship VIA', tracking=True)
    # box = fields.Boolean(string='Box', tracking=True)

    @api.onchange('packing')
    def _sale_id(self):
        for rec in self:
            rec.box_num = rec.env['stock.picking'].search(
                [('origin', '=', rec.invoice_origin)]).box_num
            print('ffffffffffffffffffffffff', rec.box_num)




    @api.depends()
    def _total_price_(self):
        for rec in self:
            rec.total_m2 = sum(rec.invoice_line_ids.mapped('quantity'))

    @api.depends()
    def _total_amount_(self):
        for rec in self:
            rec.total_amount = sum(rec.invoice_line_ids.mapped('price_subtotal'))

    @api.depends()
    def _total_container_(self):
        for rec in self:
            rec.Container_no = int(len(rec.container_num.mapped('name')))


    @api.depends()
    def _total_total_gw_(self):
        for rec in self:
            rec.total_gw = sum(rec.container_num.mapped('total_gw'))

    @api.depends()
    def _total_total_nw_(self):
        for rec in self:
            rec.total_nw = sum(rec.container_num.mapped('total_nw'))


    @api.depends()
    def _total_total_bundle_(self):
        for rec in self:
            rec.total_bundle = sum(rec.container_num.mapped('total_bundle'))


    @api.depends()
    def _total_total_pallets_(self):
        for rec in self:
            rec.total_pallets = sum(rec.container_num.mapped('total_pallets'))

    @api.depends()
    def _total_box_(self):
        for rec in self:
            rec.box_no = int(len(rec.box_num.mapped('box_num_id')))

    @api.depends('invoice_origin', 'user_id', 'company_id')
    def _compute_sale_order_name(self):
        for rec in self:
            query = self.env['sale.order'].search(
                [('name', '=', self.invoice_origin),
                 ('user_id', '=', self.invoice_user_id.id),
                 ('company_id', '=', self.company_id.id)]).name
            if query:
                rec.sale_order_num = query
            else:
                rec.sale_order_num == 'unknown'
