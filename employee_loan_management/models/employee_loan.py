from odoo import api, fields, models, tools
from odoo.exceptions import ValidationError


class EmployeeLoan(models.Model):
    _name = 'employee.loan'
    _inherit = ['mail.thread']

    employee_id = fields.Many2one(comodel_name='hr.employee', string="Employee",domain=[('loan_not_allowed','=',False)])
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
        readonly=True)
    loan_amount = fields.Monetary(string="Loan Amount", currency_field='currency_id', default=0)
    installment_count = fields.Integer(string="Installment Count")
    start_date = fields.Date(string="Start Date")
    state = fields.Selection([('draft', 'Draft'), ('approved', 'Approved'), ('ongoing', 'Ongoing'), ('paid', 'Paid')],
                             "State", default='draft')
    loan_line_ids = fields.One2many('employee.loan.line', 'loan_id', string="Loan Lines")
    name = fields.Char(
        string="Employee Name",
        required=True, copy=False, readonly=True,
        default=lambda self: ('New'))
    installment_amount = fields.Monetary(string="Installment Amount",
                                         currency_field='currency_id')
    total_payable = fields.Monetary(string="Total Payable", compute='_compute_payable_amount',store=True,
                                    currency_field='currency_id',)
    loan_line_count = fields.Integer(string="Loan Line Count", compute='_compute_loan_line_count',store=True)
    paid_amount = fields.Monetary(string="Paid Amount", compute='_compute_paid_amount', currency_field='currency_id',store=True)
    balance_amount = fields.Monetary(string="Balance Amount", compute='_compute_balance_amount',
                                     currency_field='currency_id',store=True)

    @api.depends('loan_line_ids.paid')
    def _compute_paid_amount(self):
        self.paid_amount = sum(self.loan_line_ids.search([('loan_id','=',self.id),('paid', '=', True)]).mapped('amount'))
        print(5678,self.loan_line_ids.search([('loan_id','=',self.id),('paid', '=', True)]))



    @api.depends('paid_amount')
    def _compute_balance_amount(self):
        for record in self:
            record.balance_amount = record.total_payable - record.paid_amount
            print(1234,record.balance_amount)


    @api.depends('loan_line_ids')
    def _compute_loan_line_count(self):
        """CALCULATE THE INVOICE COUNT FOR SMART BUTTON"""
        for record in self:
            record.loan_line_count = len(record.loan_line_ids)

    @api.onchange('loan_amount', 'installment_count')
    def _onchange_installment_amount(self):
        if self.loan_amount > 0:
            if self.installment_count > 0:
                self.installment_amount = self.loan_amount / self.installment_count
            else:
                self.installment_amount = 0

        else:
            self.installment_amount = 0

    @api.depends('loan_amount')
    def _compute_payable_amount(self):
        for record in self:
            record.total_payable = record.loan_amount
            # record.write({'total_payable':record.loan_amount})

    @api.model_create_multi
    def create(self, vals_list):
        """SEQUENCE CREATION FOR ROOM RECORD"""
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = (self.env['ir.sequence'].
                                next_by_code('employee.loan') or 'New')
        return super(EmployeeLoan, self).create(vals_list)

    def action_approve(self):
        if self.loan_amount > 0 and self.installment_count > 0:
            self.state = 'approved'
        else:
            raise ValidationError('Loan amount & installment count must be greater than 0')

    def action_get_invoice_records(self):
        """GET INVOICE RECORD OF ROOM FOR SMART BUTTON"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Installments',
            'view_mode': 'list,form',
            'res_model': 'employee.loan.line',
            'domain': [('id', 'in', self.loan_line_ids.ids)],
            'context': {'create': False}
        }

    def action_create_installment(self):
        self.state = 'ongoing'
        i=0
        while i < self.installment_count:
            self.env['employee.loan.line'].create({
                'loan_id': self.id,
                'amount': self.installment_amount
            })
            i +=1

    def action_pay_installment(self):
        result = self.loan_line_ids.search([('paid', '=', False)]).sorted('id')
        for record in result:
            record.paid = True
            break
        result = self.loan_line_ids.search([('paid', '=', False)])
        print(1234,result)

        if not result:
            self.state = 'paid'
