from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_amount_limit = fields.Integer(related='pos_config_id.discount_amount_limit', readonly=False)


