from openpyxl.worksheet import related

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    restricted = fields.Boolean(related="partner_id.restricted", string="Restricted", default=False)
    restricted_count = fields.Integer(related="partner_id.restricted_count", string="Restricted Count", default=0)

    @api.onchange('order_line')
    def _compute_restricted(self):

        for record in self:
            if len(self.order_line) > record.restricted_count and record.restricted:
                raise ValidationError("Can not create line more than restricted count")
