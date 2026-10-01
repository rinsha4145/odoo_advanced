from email.policy import default

from odoo import api, fields, models, tools

class ResPartner(models.Model):
    _inherit = 'res.partner'

    restricted=fields.Boolean(string="Restricted",default=False)
    restricted_count = fields.Integer(string="Restricted Count",default=0)