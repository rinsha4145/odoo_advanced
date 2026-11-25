from odoo import models, fields
from datetime import datetime


class InventoryDashboard(models.Model):
    _name = 'inventory.dashboard'

    def date_fetch(self, date):
        if date.get('year') != False and date.get('month') != False:
            base_dt = datetime(date.get('year'), date.get('month'), 1)
            start_dt = fields.Datetime.start_of(base_dt, 'month')
            end_dt = fields.Datetime.end_of(base_dt, 'month')
            return [
                '&',('create_date', '<=', start_dt), ('create_date', '>=', end_dt)
            ]
        # elif date.get('year') != False and date.get('month') == False:
        return False

    def action_fetch(self, date):

        domain = self.date_fetch(date)
        if domain:
            # stock incoming &outgoing by product wise
            print(56, domain)
            product_stock = self.env['product.template'].search_read(
                ['|', ('incoming_qty', '>', 0), ('outgoing_qty', '>', 0)].append(domain),
                ['name', 'incoming_qty', 'outgoing_qty'])
            # Group based on picking type
            picking_group = self.env['stock.picking']._read_group(
                [('state', 'not in', ['cancel'])], ['picking_type_id.code'], ['__count']

            )
        else:
            product_stock = self.env['product.template'].search_read(
                ['|', ('incoming_qty', '>', 0), ('outgoing_qty', '>', 0)],
                ['name', 'incoming_qty', 'outgoing_qty'])
            # Group based on picking type
            picking_group = self.env['stock.picking']._read_group(
                [('state', 'not in', ['cancel'])], ['picking_type_id.code'], ['__count']

            )
        # Average expense of  a product(purchase cost + landed cost)
        products = self.env['product.product'].search([])
        stock_valuation = self.env['stock.valuation.adjustment.lines'].sudo()
        avg_expense_by_product = []
        for product in products:
            base_domain = [('product_id', '=', product.id), ('quantity', '>', 0),
                           ("additional_landed_cost", "!=", False)]
            if domain:
                result = stock_valuation.search(base_domain + domain)
                print(678, result)

            else:
                result = stock_valuation.search(base_domain)
            total_qty = sum(result.mapped('quantity'))
            total_cost = sum(result.mapped('final_cost'))
            avg_expense_cost = total_cost / total_qty if total_qty else 0.0
            if result:
                avg_expense_by_product.append({
                    'product_id': result.product_id.name,
                    'cost': round(avg_expense_cost, 2)
                })

        # Internal transfers(Product wise)
        if self.env.user.has_group('stock.group_stock_manager'):
            internal_transfer_move = self.env['stock.move']._read_group(
                [('state', '=', 'done'), ('picking_type_id.code', '=', 'internal')],
                ['product_id.name'], ['quantity:sum']

            )
        else:
            internal_transfer_move = self.env['stock.picking']._read_group(
                [('state', '=', 'done'), ('picking_type_id.code', '=', 'internal'), ('user_id', '=', self.env.user.id)],
                ['product_id.name'], ['quantity:sum']
            )
        print(1234567, internal_transfer_move)
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

        }
