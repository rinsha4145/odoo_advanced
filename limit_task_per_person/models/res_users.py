from odoo import api, models,fields


class ResUsers(models.Model):
    _inherit = "res.users"

    task_limit = fields.Integer(string="Task Limit")