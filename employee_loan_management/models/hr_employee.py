from odoo import api, fields, models, exceptions

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    loan_not_allowed=fields.Boolean(string="Not Allowed")