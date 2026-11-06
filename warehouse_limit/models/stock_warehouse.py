
from odoo import api, fields, models


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    quantity_limit = fields.Integer(string="Quantity Limit")

