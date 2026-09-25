from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    sale_order_ids = fields.Many2many('sale.order', string="Sale Order", domain="[('invoice_ids','=',False)]",compute="_compute_sale_order_ids",store=True)

    @api.depends('sale_order_ids')
    def _compute_sale_order_ids(self):
        for sale in self.sale_order_ids:
            print(sale)
            for line in sale.order_line:
                print(line)
                invoice_lines=[]
                self.invoice_line_ids.create(
                    {'product_id': line.product_id, 'quantity': line.product_uom_qty, 'price_unit': line.price_unit,
                     'tax_ids': line.tax_ids.ids, 'price_subtotal': line.price_subtotal})
