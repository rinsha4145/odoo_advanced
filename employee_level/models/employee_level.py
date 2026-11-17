from odoo import fields,models

class EmployeeLevel(models.Model):
    _name = 'employee.level'
    _rec_name = 'level'

    level = fields.Char(string="Level",required=True)
    salary = fields.Float(string="Salary",required=True)
    sequence = fields.Integer(string="Sequence")

