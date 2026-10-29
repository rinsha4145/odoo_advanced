from odoo import fields, models, api


class PosConfig(models.Model):
    _inherit = 'pos.config'

    discount_amount_limit = fields.Integer(string="Discount Limit", readonly=False)
    total_discount_amount = fields.Float(string='total discount amount', readonly=True, default=0)

    # @api.model
    # def _load_pos_data_fields(self, config_id):
    #     """Return fields to be loaded into the POS."""
    #     print(9999)
    #     data = super()._load_pos_data_fields(config_id)
    #     data += ['discount_amount_limit', 'total_discount_amount']
    #     print(12345, data)
    #     return data
