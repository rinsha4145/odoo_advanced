from odoo import api, fields, models, tools

class ProductTemplate(models.Model):
    _inherit = 'stock.location'

    def action_fetch(self):
        print(234567)
        print(123,self[0].read())

        return {
            "location":self.env['stock.location'].search_read(
                [ ('quant_ids', '!=', False)], ['complete_name', 'quant_ids', 'warehouse_id']),
        }
