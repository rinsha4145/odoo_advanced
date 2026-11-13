from odoo import api, fields, models, tools


class fleet_service_order_checklist(models.Model):
    _name = 'fleet.service.order.checklist'
    _description = 'fleet.service.order.checklist'

    order_id = fields.Many2one('fleet.service.order',string='Order')
    task_name = fields.Char(string="Task Name")
    is_done = fields.Boolean(string="Is Done")
    note = fields.Text(string="Note")
