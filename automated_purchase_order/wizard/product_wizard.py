from odoo import api, fields, models, Command
from odoo.exceptions import UserError


class ProductTemplate(models.TransientModel):
    _name = 'product.wizard'

    quantity = fields.Integer(string='Quantity', default=1)
    product_id = fields.Many2one('product.product', string='Product',
                                 default=lambda self: self.env.context.get('dafult_product_id'))
    price = fields.Float(string='Price')
    vendor_id = fields.Many2one('res.partner', string='Vendor')

    @api.onchange('quantity')
    def _onchange_quantity(self):
        """TAKE FIRST VENDOR OF PRODUCT """
        vendor = self.product_id.seller_ids.filtered(lambda p: p.min_qty <= self.quantity).sorted('min_qty DESC,price ')[:1]
        # vendor = self.product_id.seller_ids[:1]
        # self.vendor_id = vendor.id

        self.write({'vendor_id': vendor.partner_id.id, 'price': vendor.price})
        # self.price = vendor.price
        print(9876, self.vendor_id)

    def action_confirm(self):
        """CREATE A PURCHASE ORDER"""
        print(4567, self.read())
        if self.quantity > 0:
            if self.vendor_id:
                purchase_order_exist = self.env['purchase.order'].search(
                    [('state', '=', 'draft'), ('partner_id', '=', self.vendor_id)])
                print(4567, purchase_order_exist)
                if purchase_order_exist:
                    is_added = False
                    for purchase_order in purchase_order_exist:
                        for line in purchase_order.order_line:
                            print(3333, line)
                            if line.product_id == self.product_id and is_added == False:
                                line.write({'product_qty': self.quantity + line.product_qty, 'price_unit': self.price})
                                is_added = True
                    print(222, is_added)
                    if is_added == False:
                        latest_purchase_order = purchase_order_exist.sorted('create_date')[:1]
                        print(4444, latest_purchase_order.read())

                        po_line = self.env['purchase.order.line'].create({
                            'order_id': latest_purchase_order.id,
                            'product_id': self.product_id.id,
                            'name': self.product_id.name,
                            'product_qty': self.quantity,
                            'price_unit': self.price,
                        })
                        print(66666, po_line)
                        latest_purchase_order.order_line = [Command.link(po_line.id)]
                        print(5555, latest_purchase_order.read())
                else:
                    po = self.env['purchase.order'].create({
                        'partner_id': self.vendor_id.id,
                    })
                    self.env['purchase.order.line'].create({
                        'order_id': po.id,
                        'product_id': self.product_id.id,
                        'name': self.product_id.name,
                        'product_qty': self.quantity,
                        'price_unit': self.price,
                    })
            else:
                raise UserError(('Add A Vendor Who Have %s Quantity As Minimum Quantity') % self.quantity)

        else:

            raise UserError('Add a Quantity')
        # return {'type': 'ir.actions.act_window_close'}
