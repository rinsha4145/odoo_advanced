from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    sale_order_ids = fields.Many2many('sale.order', string="Sale Order",
                                      domain="[('invoice_status','!=','invoiced'),('state','=','sale')]")

    @api.onchange('sale_order_ids')
    def _onchange_sale_order_ids(self):
        for invoice in self:
            manual_lines = invoice.invoice_line_ids.filtered(lambda line: not line.sale_line_id)
            invoice.invoice_line_ids = manual_lines
            print(invoice.invoice_line_ids)
            for order_line_i in manual_lines:
                print("kkkk",order_line_i.product_id)
            a = []

            for sale in invoice.sale_order_ids:
                for order_line in sale.order_line:
                    print(order_line)
                    if order_line.display_type  :
                        continue

                    a.append ((0,0,
                        {'move_id':self.id,'product_id': order_line.product_id.id, 'quantity': order_line.product_uom_qty,
                         'price_unit': order_line.price_unit,'sale_line_id':order_line.id}))

            invoice.invoice_line_ids += a
