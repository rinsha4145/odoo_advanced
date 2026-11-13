from odoo import api, fields, models, _


class FleetServiceOrder(models.Model):
    _name = 'fleet.service.order'
    _description = 'Fleet Service Order'

    name = fields.Char(
        string="Service Name",
        required=True, copy=False, readonly=True,
        default=lambda self: ('New'))
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle', required=True)
    technician_id = fields.Many2one('hr.employee', string='Technician', required=True)
    service_date = fields.Date(string='Service Date', required=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('in_progress', 'In Progress'), ('done', 'Done'),
         ('cancelled', 'Cancelled')])
    part_ids = fields.One2many('fleet.service.order.part', 'order_id', string='Parts')
    checklist_ids = fields.One2many('fleet.service.order.checklist', 'order_id', string='Checklist')

    @api.model_create_multi
    def create(self, vals_list):
        """SEQUENCE CREATION FOR ROOM RECORD"""
        for vals in vals_list:
            print(4567890)
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('fleet.service.order') or _('New')
                print(vals['name'])
        return super(FleetServiceOrder, self).create(vals_list)
