from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    about = fields.Char( string='About',readonly=False)
    count = fields.Integer(readonly=False)