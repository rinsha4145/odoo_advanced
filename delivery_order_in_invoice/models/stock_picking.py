from odoo import api, fields, models, tools


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    invoice_id = fields.Many2one('account.move',string="Invoice")