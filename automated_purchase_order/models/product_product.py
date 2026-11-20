from odoo import models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def action_open_wizard(self):
        """PURCHASE ORDER CREATION WIZARD OPEN"""
        self.ensure_one()
        return {
            'name': 'Create Purchase Order',
            'view_mode': 'form',
            'res_model': 'product.wizard',
            'target': 'new',
            'type': 'ir.actions.act_window',
            'context': {'dafult_product_id':self.id}
        }
