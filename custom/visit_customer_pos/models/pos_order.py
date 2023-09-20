from odoo import fields, models, api, _
from odoo.exceptions import UserError



class pos_order_line(models.Model):
    _inherit = 'pos.order'

    visit_customer_id = fields.Many2one(
        comodel_name='visit.customer.pos',
        string=' Category',
        required=False)

    @api.ondelete(at_uninstall=False)
    def _unlink_except_draft_or_cancel(self):
        for pos_order in self.filtered(lambda pos_order: pos_order.state in ['draft', 'cancel']):
            raise UserError(_('In order to delete a sale, it must be new or cancelled.'))



