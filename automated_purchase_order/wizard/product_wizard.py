from odoo import api, fields, models, tools

class ProductTemplate(models.TransientModel):
    _name = 'product.wizard'

    quantity = fields.Integer(string='Quantity')
    price  = fields.Float(string='Price')
    product_id = fields.Many2one('product.product')
