from odoo import models


class InventoryDashboard(models.Model):
    _name = 'inventory.dashboard'

    def action_fetch(self):
        # stock incoming &outgoing by product wise
        product_stock = self.env['product.template'].search_read(
            ['|', ('incoming_qty', '>', 0), ('outgoing_qty', '>', 0)], ['name', 'incoming_qty', 'outgoing_qty'])

        # Average expense of  a product(purchase cost + landed cost)
        products = self.env['product.product'].search([])
        stock_valuation = self.env['stock.valuation.adjustment.lines']
        avg_expense_by_product = []
        for product in products:
            result = stock_valuation.search(
                [('product_id', '=', product.id), ('quantity', '>', 0), ("additional_landed_cost", "!=", False)])
            total_qty = sum(result.mapped('quantity'))
            total_cost = sum(result.mapped('final_cost'))
            avg_expense_cost = total_cost / total_qty if total_qty else 0.0
            avg_expense_by_product.append({
                'product_id': result.product_id.name,
                'cost': round(avg_expense_cost, 2)
            })
        # Group based on picking type
        picking_group = self.env['stock.picking']._read_group(
            [('state', 'not in', ['done', 'cancel'])],['picking_type_id.code'],['__count']

        )

        # Internal transfers(Product wise)

        internal_transfer_move = self.env['stock.move']._read_group(
            [('state', '=', 'done'), ('picking_type_id.code', '=', 'internal')], ['product_id'], ['product_qty:sum']

        )
        print(99,internal_transfer_move)
        # locations = self.env["stock.location"].search(
        #     [("warehouse_id", "=", recordId), ("quant_ids", '!=', False)], )
        # quant_groups = self.env['stock.quant'].read_group(
        #     domain=[('location_id', 'in', locations.ids), ('quantity', '>', 0)],
        #     fields=['location_id', 'quantity:sum', 'reserved_quantity:sum'],
        #     groupby=['location_id']
        # )
        # print(quant_groups)

        # ["complete_name", "quant_ids", "usage", "location_id", 'warehouse_id']

        # all_done_moves = self.env['product.template'].search([('state', '=', 'done')])
        # for move in all_done_moves:

        # "location": self.env['stock.location'].search_read(
        #     [('quant_ids', '!=', False)], ['complete_name', 'quant_ids', 'warehouse_id']),

        return {
            'product_stock': product_stock,
            "avg_expense_by_product": avg_expense_by_product,
            "picking_group": picking_group,
            "internal_transfer_move": internal_transfer_move,
            # 'locations': locations,

        }
