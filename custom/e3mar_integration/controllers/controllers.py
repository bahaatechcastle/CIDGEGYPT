# -*- coding: utf-8 -*-
# from odoo import http


# class E3marIntegration(http.Controller):
#     @http.route('/e3mar_integration/e3mar_integration', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/e3mar_integration/e3mar_integration/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('e3mar_integration.listing', {
#             'root': '/e3mar_integration/e3mar_integration',
#             'objects': http.request.env['e3mar_integration.e3mar_integration'].search([]),
#         })

#     @http.route('/e3mar_integration/e3mar_integration/objects/<model("e3mar_integration.e3mar_integration"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('e3mar_integration.object', {
#             'object': obj
#         })
