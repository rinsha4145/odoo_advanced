
from odoo import api, fields, models


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    product_quantity_limit = fields.Integer(string="Quantity Limit")

