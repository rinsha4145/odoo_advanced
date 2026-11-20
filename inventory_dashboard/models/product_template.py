from odoo import api, fields, models, tools

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_fetch(self):

