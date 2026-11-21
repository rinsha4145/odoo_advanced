from odoo import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_fetch(self):
        return {
            'product_stock': self.env['product.template'].search_read(
                ['|', ('incoming_qty', '>', 0), ('outgoing_qty', '>', 0)], ['name', 'incoming_qty', 'outgoing_qty']),


        }
