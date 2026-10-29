from odoo import fields, models, api

class PosSession(models.Model):
    _inherit = 'pos.session'

    total_discount_amount = fields.Float(string='total discount amount', readonly=True,default=0)

    # @api.model
    # def _compute_total_discount(self):
    #     for session in self:
    #         s = session.order_ids.lines.mapped('discount')
    #         print(89,s)

    @api.model
    def _load_pos_data_fields(self, config_id):
        """Return fields to be loaded into the POS."""
        data = super()._load_pos_data_fields(config_id)
        data += ['total_discount_amount']
        print(12345, data)
        return data