from odoo import api, fields, models

class ProductLine(models.Model):
    _name = 'product.line'

    order_id = fields.Many2one('sale.order',string='Order')
    selected_product_ids = fields.Many2many('product.product', string='Products')
    product_quantity = fields.Integer(string='Quantity')
