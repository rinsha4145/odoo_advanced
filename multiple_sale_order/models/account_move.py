from odoo import models, fields, api, Command


class AccountMove(models.Model):
    _inherit = "account.move"

    sale_order_ids = fields.Many2many('sale.order', string="Sale Order",
                                      domain=" [('invoice_status', '=', 'to invoice'),('partner_id', '=', partner_id)]")

    @api.onchange('sale_order_ids')
    def _onchange_sale_order_ids(self):
        for invoice in self:
            invoice_lines = []
            for sale in invoice.sale_order_ids:
                invoice.invoice_line_ids = [Command.clear()]
                for order_line in sale.order_line:
                    invoice_lines.append(Command.create(
                        {'product_id': order_line.product_id.id,
                         'quantity': order_line.product_uom_qty,
                         'price_unit': order_line.price_unit,
                         }))

            invoice.invoice_line_ids = invoice_lines

    def write(self, vals):
        res = super().write(vals)
        for invoice in self:
            if not invoice.sale_order_ids:
                super(AccountMove, invoice).write({'invoice_line_ids': [Command.clear()]})
            else:
                for sale in invoice.sale_order_ids:
                    for order_line in sale.order_line:
                        invoice_line = invoice.invoice_line_ids.filtered(
                            lambda line: line.product_id == order_line.product_id )
                        if invoice_line:
                            invoice_line.write({'sale_line_ids': [Command.link(order_line.id)]})
                    for invoice_line in invoice.invoice_line_ids:
                        print(invoice_line.sale_line_ids)

        return res
