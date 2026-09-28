import typing

from odoo import models, fields, api , Command


class AccountMove(models.Model):
    _inherit = "account.move"

    sale_order_ids = fields.Many2many('sale.order', string="Sale Order",
                                      domain=" [('invoice_status', '=', 'to invoice'),('partner_id', '=', partner_id)]")

    @api.onchange('sale_order_ids')
    def _onchange_sale_order_ids(self):
        for invoice in self:
            invoice_line = []
            for sale in invoice.sale_order_ids:
                invoice.invoice_line_ids = False
                for order_line in sale.order_line:
                    invoice_line.append((0, 0,
                                         {'product_id': order_line.product_id.id,
                                          'quantity': order_line.product_uom_qty,
                                          'price_unit': order_line.price_unit}))

            invoice.invoice_line_ids = invoice_line



    # def action_post(self):
    #     super()._create_invoices()
    #     print(7890)
    #
    def write(self, vals):
        res =  super().write(vals)
        for invoice in self:
            for sale in invoice.sale_order_ids:
                sale.write({'invoice_ids': [Command.link(invoice.id)]})
                sale.invalidate_recordset(['invoice_ids'])
                for i in sale.invoice_ids:
                    print(5678, i.id)
        return res
