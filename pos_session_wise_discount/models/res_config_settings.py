from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_amount_limit = fields.Integer(related='pos_config_id.discount_amount_limit', readonly=False)
    total_discount_amount = fields.Float(related='pos_config_id.total_discount_amount',
                                           string='total discount amount', readonly=False,  )

