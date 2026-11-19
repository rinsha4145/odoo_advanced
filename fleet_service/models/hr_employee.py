from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    is_available_technician  = fields.Boolean(string="Technician")
    vehicle_ids = fields.Many2many('fleet.vehicle',string="Vehicle IDs",)
