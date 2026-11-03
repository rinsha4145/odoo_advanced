from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    api_key = fields.Char(related="company_id.api_key",readonly=False)