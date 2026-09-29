from odoo import api, fields, models, Command

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    associated_product = fields.Boolean(string="Associated Product",default=False)

    @api.onchange('associated_product')
    def onchange_associated_product(self):
        """get the associated product from the customer"""
        for record in self:
            order_lines = []
            products = record.partner_id.product_ids
            if record.associated_product:
                if record.order_line.product_id != products:
                    print(900)
                    for product in products:
                        print(777)
                        order_lines.append(Command.create(
                            {'product_id' : product,
                             }))
                    record.order_line = order_lines

