from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    about = fields.Char( string='About')
    counter_max = fields.Integer(string='Max Counter Value',)