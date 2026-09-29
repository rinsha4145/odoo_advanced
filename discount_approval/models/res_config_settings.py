from odoo import fields, models
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_limit = fields.Float(string="Discount Limit" ,config_parameter='discount_approval.discount')