# -*- coding: utf-8 -*-
# from odoo import http


# class InvoiceReportCidg(http.Controller):
#     @http.route('/invoice_report__cidg/invoice_report__cidg', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_report__cidg/invoice_report__cidg/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_report__cidg.listing', {
#             'root': '/invoice_report__cidg/invoice_report__cidg',
#             'objects': http.request.env['invoice_report__cidg.invoice_report__cidg'].search([]),
#         })

#     @http.route('/invoice_report__cidg/invoice_report__cidg/objects/<model("invoice_report__cidg.invoice_report__cidg"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_report__cidg.object', {
#             'object': obj
#         })
