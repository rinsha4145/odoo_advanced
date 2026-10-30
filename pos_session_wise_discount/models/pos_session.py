from odoo import fields, models, api

class PosSession(models.Model):
    _inherit = 'pos.session'

    total_discount_amount = fields.Float(string='total discount amount', readonly=True,default=0)


    @api.model
    def _load_pos_data_fields(self, config_id):
        """Return fields to be loaded into the POS."""
        data = super()._load_pos_data_fields(config_id)
        data += ['total_discount_amount']
        return data