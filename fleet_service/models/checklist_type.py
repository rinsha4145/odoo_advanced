from odoo import models,fields,api


class ChecklisType(models.Model):
    _name = 'checklist.type'
    _description = 'Checklist Type'

    name = fields.Char(string='Name')