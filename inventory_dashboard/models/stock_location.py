from odoo import api, fields, models, tools

class ProductTemplate(models.Model):
    _inherit = 'stock.location'

    def action_fetch(self):
        print(self[0].read())

        return {
            "yyyr":'fhbrfh'
        }
