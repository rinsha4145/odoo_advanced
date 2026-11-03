from odoo import fields, models

class ResCompany(models.Model):
    _inherit = "res.company"

    api_key = fields.Char(string="API Key")
