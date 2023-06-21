# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _
from odoo.exceptions import ValidationError, RedirectWarning, UserError
import logging

logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    email_parent = fields.Char(string='Email Parent', default=False,)
    phone_whatsapp = fields.Char(string='Phone Whatsapp', default=False,)
    phone_2 = fields.Char(string='Phone 2', default=False,)
    profession = fields.Char(string='Profession', default=False,)
    note = fields.Text(string='Profession', default=False,)
    # parent_name = fields.Many2one('res.partner' ,string='Parent Name')
    parent_name = fields.Char(string='Parent Name')
    # source = fields.Many2one('utm.source' ,string='Source')
    source = fields.Char(string='Source')

    

        
    