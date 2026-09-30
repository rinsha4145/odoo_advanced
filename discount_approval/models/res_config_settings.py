from odoo import fields, models,api
from odoo.tools import ormcache


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    so_double_validation_amount = fields.Float(related='company_id.so_double_validation_amount',readonly=False)
    so_order_approval = fields.Boolean(related='company_id.so_order_approval',string="Order Approval",readonly=False)

