from odoo import api, fields, models, _, Command
from odoo.exceptions import ValidationError


class FleetServiceOrder(models.Model):
    _name = 'fleet.service.order'
    _description = 'Fleet Service Order'

    name = fields.Char(
        string="Service Name",
        required=True, copy=False, readonly=True,
        default=lambda self: ('New'))
    technician_id = fields.Many2one('hr.employee', string='Technician',domain="[('is_available_technician','=','True')]")
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle', required=True,)

    service_date = fields.Date(string='Service Date')
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('in_progress', 'In Progress'), ('done', 'Done'),
         ('cancelled', 'Cancelled')], copy=False, default='draft')
    part_ids = fields.One2many('fleet.service.order.part', 'order_id', string='Parts')
    checklist_ids = fields.One2many('fleet.service.order.checklist', 'order_id', string='Checklist')
    parts_total = fields.Float(string='Total Parts', stored=True, compute='_compute_total',copy=False)
    labour_cost = fields.Float(string='Labour Cost')
    grand_total = fields.Float(string='Grand Total', compute='_compute_grand_total', stored=True,copy=False)
    checklist_progress = fields.Float(string='Checklist Progress', compute='_compute_checklist_progress',stored=True,copy=False)
    type_ids = fields.Many2many('checklist.type', string='Types')
    domain = fields.Char(compute='_compute_has_domain')

    @api.depends('technician_id')
    def _compute_has_domain(self):
        if self.technician_id:
            self.domain = [('service_blocked','=',False),('id', 'in', self.technician_id.vehicle_ids.ids)]
        else:
            self.domain = [('service_blocked','=',False)]


    def write(self, vals):
        result = super().write(vals)
        if self.state=='in_progress' and  self.checklist_progress == 100:
            self.state = 'done'
        return result

    # @api.onchange('technician_id')
    # def _onchange_technician(self):787
    #     self.vehicle_id
    # @api.onchange('technician_id')
    # def _onchange_field_a(self):
    #     if self.technician_id and self.vehicle_id not in self.technician_id.b_ids:
    #         self.field_b = False
    @api.model_create_multi
    def create(self, vals_list):
        """SEQUENCE CREATION FOR ROOM RECORD"""
        for vals in vals_list:
            print(4567890)
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('fleet.service.order') or _('New')
                print(vals['name'])
        return super(FleetServiceOrder, self).create(vals_list)

    @api.depends('part_ids')
    def _compute_total(self):
        self.parts_total = sum(part.quantity * part.unit_price for part in self.part_ids)

    @api.depends('parts_total', 'labour_cost')
    def _compute_grand_total(self):
        self.grand_total = self.parts_total + self.labour_cost

    @api.depends('checklist_ids.is_done')
    def _compute_checklist_progress(self):
        result = self.checklist_ids.search_count([('is_done', '=', 'True'),('order_id', '=',self.id)])
        if result > 0 and len(self.checklist_ids) > 0 :
            self.checklist_progress = result / len(self.checklist_ids)  * 100
        else:
            self.checklist_progress = 0


    def action_state_change(self):
        if len(self.part_ids) > 0 and self.part_ids[0].quantity > 0:
            self.state = 'confirmed'
        else:
            raise ValidationError('add at least one part line and have quantity')

    def action_start(self):
        if self.technician_id:
            print(34,self.technician_id)
            self.state = 'in_progress'
        else:
            raise ValidationError('Add a technician')

    def action_cancel(self):
        self.state = 'cancelled'


    def action_generate(self):
        warning = []
        for type in self.type_ids:
            if type.name not in self.checklist_ids.mapped('task_name'):
                self.checklist_ids = [Command.create({
                    'task_name': type.name,
                    'order_id': self.id
                })]
            else:
                warning.append(type.name)
        if warning:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Warning!',
                    'message': f"{', '.join(warning)} already exist in checklist",
                    'type': 'warning',
                    'sticky': False,
                    'next':{'type':'ir.actions.client','tag':'soft_reload'}
                }
            }
