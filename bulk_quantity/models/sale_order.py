from odoo import api, fields, models, Command
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    product_line_id = fields.One2many('product.line','order_id',string='Product')

    def action_add_to_order_line(self):
        for order in self:
            if order.product_quantity <= 0:
                raise ValidationError("jnknk")
            for product in order.selected_product_ids:
                existing_line = []
                if existing_line:
                    print(99)
                else:
                    self.env['sale.order.line'].create({
                        'order_id': order.id,
                        'product_id': product.id,
                        'product_uom_qty': order.product_quantity
                    })
                    order.write({'product_quantity': 0,
                                 'selected_product_ids': Command.clear()})
