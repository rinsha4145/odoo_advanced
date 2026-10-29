from odoo import fields, models, api

class PosSession(models.Model):
    _inherit = 'pos.session'

    total_discount_amount = fields.Integer(string='Total Discount',compute='_compute_total_discount')

    @api.model
    def _compute_total_discount(self):
        for session in self:
            s = session.order_ids.lines.mapped('discount')
            print(89,s)