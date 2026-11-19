from odoo import api, fields, models, tools
class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    service_blocked = fields.Boolean(string="Service Blocked")