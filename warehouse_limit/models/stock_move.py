from odoo import api, fields, models
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    # def _compute_quantities(self):
    #     super()._compute_quantities()
    #
    #     warehouse = self.env['stock.warehouse'].search([('company_id', '=', self.env.company.id)], limit=1)
    #     for product in self:
    #         stock = self.env['stock.quant'].search([('product_id', '=', product.id),('warehouse_id', '!=', False)])
    #         print(1234,sum(stock.mapped('inventory_quantity_auto_apply')))
    #         # for s in stock:
    #         #     for warehouse in s.warehouse_id:
    #                 # value = sum(warehouse.mapped('inventory_quantity_auto_apply'))
    #                 # print(34567, value)
    def button_validate(self):
        res = super().button_validate()
        for move in self.move_ids:
            print(234232, move.location_dest_id.usage)
            if move.location_dest_id.usage == 'internal':
                warehouse = self.env['stock.warehouse'].search(
                    [('lot_stock_id', 'parent_of', move.location_dest_id.id)], limit=1)
                print(234, warehouse.read())

                if warehouse and warehouse.quantity_limit > 0:
                    locations = self.env['stock.location'].search(
                        [('id', 'child_of', warehouse.view_location_id.id)]).ids

                    print(234, locations)
                    stock = self.env['stock.quaunt'].search(
                        [('location_id', 'in', locations)])
                    print(9999999, stock)

                    sum_of_qty = sum(stock.mapped('quantity'))
                    total = sum_of_qty + sum(move.mapped('product_uom_qty'))

                    print(2345, stock.read())
                    if total > warehouse.quantity_limit:
                        raise UserError("%s remaining space in the warehouse" % (sum_of_qty - warehouse.quantity_limit))
        return res

# def _action_done(self, cancel_backorder=False):
#     res = super()._action_done(cancel_backorder=cancel_backorder)
#     for move in self:
#         if move.location_dest_id.usage == 'internal':
#             warehouse = self.env['stock.warehouse'].search(
#                 [('lot_stock_id', 'parent_of', move.location_dest_id.id)])
#             print(234, warehouse)
#     return res
