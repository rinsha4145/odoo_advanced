# -*- coding: utf-8 -*-
from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    approval_users = fields.Many2many('res.users',string='Approved Users')