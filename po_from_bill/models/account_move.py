from odoo import api, fields, models, tools, Command
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_generate_po(self):
        """generate a purchase order for bill"""
        self.ensure_one()
        print(self.read())
        po = self.env['purchase.order'].create({
            'partner_id': self.partner_id.id,
            'origin':self.name,
        })
        for order_line in self.invoice_line_ids:
            po_line = self.env['purchase.order.line'].create({
                'order_id': po.id,
                'product_id': order_line.product_id.id,
                'name': order_line.name,
                'product_qty': order_line.quantity,
                'price_unit': order_line.price_unit,

            })
            print(678,order_line.purchase_line_id)
            po_line.invoice_lines=[Command.link(order_line.id)]

        origins = set(self.invoice_line_ids.mapped('purchase_line_id.order_id.name'))
        self.invoice_origin = ','.join(list(origins))
        po.invoice_ids = [Command.link(self.id)]



