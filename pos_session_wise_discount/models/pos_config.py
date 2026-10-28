from odoo import fields, models,api


class PosConfig(models.Model):
    _inherit = 'pos.config'

    discount_amount = fields.Integer(string="Discount Limit", readonly=False)


