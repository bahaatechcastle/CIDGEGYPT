

from odoo import models


class PosSession(models.Model):
    _inherit = "pos.session"

    def _loader_params_res_partner(self):
        res = super()._loader_params_res_partner()
        res["search_params"]["fields"].append("text_test")
        res["search_params"]["fields"].append("email_parent")
        res["search_params"]["fields"].append("phone_whatsapp")
        res["search_params"]["fields"].append("phone_2")
        res["search_params"]["fields"].append("profession")
        res["search_params"]["fields"].append("note")
        res["search_params"]["fields"].append("father_name")
        res["search_params"]["fields"].append("source")
        res["search_params"]["fields"].append("birthday_kid")
        res["search_params"]["fields"].append("age")
        return res
