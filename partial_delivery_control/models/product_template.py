from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"
    allow_partial_delivery = fields.Boolean('Partial Delivery',default=False)

