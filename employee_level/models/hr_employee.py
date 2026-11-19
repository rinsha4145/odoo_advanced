from odoo import fields, models,api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    level_id = fields.Many2one('employee.level',string="Level")
    salary = fields.Float(related ="level_id.salary",string="Salary")
    is_highest_level = fields.Boolean(string="Highest Level",compute="_compute_is_highest_level")

    def action_promote(self):
        if not self.level_id:
            value = self.env['employee.level'].search([],order='sequence ASC',limit=1)
            print(567,self.level_id.read())
        else:
            value = self.env['employee.level'].search([('sequence','>',self.level_id[0].sequence)],order='sequence ASC',limit=1)
        print(6789, value)
        if value :
            self.level_id = value.id
            print(6789,value.level)

    @api.depends('level_id')
    def _compute_is_highest_level(self):
        highest_value = self.env['employee.level'].search([],order='sequence DESC',limit=1)

        print(6789,self.level_id.sequence)
        if self.level_id == highest_value:
            self.is_highest_level = True
        else:
            self.is_highest_level = False


