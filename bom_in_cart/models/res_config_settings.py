from odoo import fields, models,api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    product_ids = fields.Many2many(related='website_id.product_ids',readonly=False,domain="[('bom_ids','!=',False)]")




