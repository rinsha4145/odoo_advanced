from odoo import fields,models
class EmployeeLoanLine(models.Model):
    _name = 'employee.loan.line'
    loan_id = fields.Many2one('employee.loan',string="Loan")
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
        readonly=True)
    date = fields.Datetime(string="Date")
    amount = fields.Monetary(string="Amount", currency_field='currency_id',store=True)
    paid = fields.Boolean(string="Paid")