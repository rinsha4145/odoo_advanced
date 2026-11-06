from odoo import api, fields, models

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    # @api.depends('quantity')
    # def _compute_inventory_quantity_auto_apply(self):
    #     res = super()._compute_inventory_quantity_auto_apply
    #     for quant in self:
    #
    #         print(23456789,quant.inventory_quantity_auto_apply)
    #     return res