import typing

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    sale_order_ids = fields.Many2many('sale.order', string="Sale Order",
                                      domain=" [('invoice_status', '=', 'to invoice'),('partner_id', '=', partner_id)]")

    @api.onchange('sale_order_ids')
    def _onchange_sale_order_ids(self):
        for invoice in self:
            manual_lines = invoice.invoice_line_ids.filtered(lambda line: line.sale_line_id)
            invoice.invoice_line_ids -= manual_lines
            invoice_line = []
            for sale in invoice.sale_order_ids:
                invoice.invoice_line_ids = False
                for order_line in sale.order_line:
                    invoice_line.append((0, 0,
                                         {'product_id': order_line.product_id.id,
                                          'quantity': order_line.product_uom_qty,
                                          'price_unit': order_line.price_unit}))
            # invoices = invoice_line.filtered(lambda line: line.sale_line_id)
            invoice.invoice_line_ids = invoice_line

    def write(self):
        for sale in self.sale_order_ids:
            sale.invoice_ids += self.id
            print(5678, sale.invoice_ids)

    def action_post(self):
        super()._create_invoices()
        print(7890)
    #
    # def write(self, vals):
    #     print(123123123)
    #     return super().write(vals)
