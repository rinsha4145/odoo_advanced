from odoo import api, fields, models, tools

class ProductTemplate(models.Model):
    _inherit = 'stock.location'

    def action_fetch(self):
        print(234567)
        print(123,self[0].read())

        return {

        }
