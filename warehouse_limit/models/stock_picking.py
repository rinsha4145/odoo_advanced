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
        for move in self:
            print(234232, move.location_dest_id)
            if move.location_dest_id.usage == 'internal':
                warehouse = move.location_dest_id.warehouse_id
                    # self.env['stock.warehouse'].search(
                    # [('lot_stock_id', 'parent_of', move.location_dest_id.id)], limit=1))
                print(234, warehouse.read())

                if warehouse and warehouse.quantity_limit > 0:
                    locations = self.env['stock.location'].search(
                        [('warehouse_id', '=', warehouse.id)]).ids
                    print(234, locations)

                    if locations:
                        stock = self.env['stock.quant'].search(
                            [('location_id', 'in', locations)])
                        total = sum(stock.mapped('quantity'))
                    # print(9999999,self.read())

                        sum_of_qty =  sum(self.move_ids.mapped('quantity'))


                        # print(454545, sum(stock.mapped('quantity')))
                        print(2345, stock.read())
                        print(3333, total)
                        if total > warehouse.quantity_limit:
                            raise UserError("%s remaining space in the warehouse"
                                            % max(warehouse.quantity_limit-(total-sum_of_qty), 0))
        return res

# def _action_done(self, cancel_backorder=False):
#     res = super()._action_done(cancel_backorder=cancel_backorder)
#     for move in self:
#         if move.location_dest_id.usage == 'internal':
#             warehouse = self.env['stock.warehouse'].search(
#                 [('lot_stock_id', 'parent_of', move.location_dest_id.id)])
#             print(234, warehouse)
#     return res
