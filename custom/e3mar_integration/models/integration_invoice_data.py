# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import json
import datetime


class e3mar_integration(models.Model):
    _inherit = 'pos.order'

    def invoice_data(self):

        # to login to the server and take token
        url1 = "https://rsmsapis.encopedia.net/webservice/RestApi/Users/Login"
        payload1 = 'userName=Mivida.Mall%40encopedia.net&password=%23Encopedia.MividaAPi%402023'
        headers1 = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-api-key': 'BST61zkrwpRMPTZxXfqY0wa17ChgX3gV',
            'Authorization': 'Basic U3RvcmVzQVBJUzpTZXJ2ZXJAc3RvcmVzYXBpLyNFbmNvcGVkaWEyMDIz'
        }
        response1 = requests.request("POST", url1, headers=headers1, data=payload1)
        data1 = response1.json()
        token = data1['result']['token']

        # to sent data to server
        invoice_data = self.env['pos.order'].search(
            [('state', '=', 'invoiced'), ('config_id.id', '=', '4'), ('config_id.name', '=', 'Mivida (New Cairo)')])

        # loop in invoice for Mivida (New Cairo)
        for rec in range(len(invoice_data)):
            x = invoice_data[-1]

            # condition to send data for today only
            if (datetime.datetime.now() - x.date_order).seconds <= 900:

                # to count discount from invoice line
                discount_product = []
                for rec in range(len(x.account_move.invoice_line_ids)):
                    discount_product.append(x.account_move.invoice_line_ids[rec].discount)
                discount = sum(discount_product)

                # url to send data
                url2 = "https://rsmsapis.encopedia.net/webservice/RestApi//Transactions/Record"

                # form json data
                info = {
                    "store": "dfa20d0a832ede096f42d22d27e75021317a18e0361d86ede8468b575a6afb2b",
                    "invoice_no": x.account_move.name,
                    "invoice_date": str(x.date_order),
                    "subtotal": x.amount_total,
                    "tax": x.amount_tax,
                    "service": "00.00",
                    "total": x.amount_paid,
                    "discount": discount
                }

                # make a list to add a form json to all invoice
                stages_list = [info]
                
                for date in range(len(stages_list)):
                    payload2 = json.dumps(
                        stages_list[date]
                    )

                #     header with token from login
                headers2 = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'x-api-key': 'BST61zkrwpRMPTZxXfqY0wa17ChgX3gV',
                    'x-token': token,
                    'Authorization': 'Basic U3RvcmVzQVBJUzpTZXJ2ZXJAc3RvcmVzYXBpLyNFbmNvcGVkaWEyMDIz'
                }
                response2 = requests.post(url2, headers=headers2, data=payload2)
                data2 = response2.json()
                print(data2)
