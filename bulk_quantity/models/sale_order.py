from odoo import api, fields, models, Command
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    selected_product_ids = fields.Many2many('product.product', string='Products')
    product_quantity = fields.Integer(string='Quantity')

    def action_add_to_order_line(self):
        for order in self:

            invoice_lines = []
            for product in order.selected_product_ids:
                existing_line = order.order_line.filtered(lambda line:line.product_id.id == product.id and not line.display_type)

                if existing_line:
                    existing_line.product_uom_qty += order.product_quantity
                else:
                    print(000)
                    invoice_lines.append(Command.create(
                        {
                            'order_id': order.id,
                            'product_id': product.id,
                            'product_uom_qty': order.product_quantity
                        }))
            order.order_line = invoice_lines
            order.write({'product_quantity': 0,
                     'selected_product_ids': [Command.clear()]})
