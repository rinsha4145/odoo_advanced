from odoo import fields, models, api
from odoo.tools import ormcache


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_amount = fields.Integer(related='pos_config_id.discount_amount', readonly=False)

    @api.model
    def _load_pos_data_fields(self, config_id):
        """Return fields to be loaded into the POS."""
        data = super()._load_pos_data_fields(config_id)
        data.append('discount_amount')
        print(12345, data)
        return data
