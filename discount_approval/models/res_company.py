# -*- coding: utf-8 -*-
from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    so_double_validation_amount = fields.Float(
        string="Minimum Amount",currency_field='company_currency_id')

    so_order_approval = fields.Boolean(string="Discount Approval", default=False)
