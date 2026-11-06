from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _compute_quantities(self):
        super()._compute_quantities()

        warehouse = self.env['stock.warehouse'].search([('company_id', '=', self.env.company.id)], limit=1)
        for product in self:
            stock = self.env['stock.quant'].search([('product_id', '=', product.id),('warehouse_id', '!=', False)])
            print(1234,sum(stock.mapped('inventory_quantity_auto_apply')))
            # for s in stock:
            #     for warehouse in s.warehouse_id:
                    # value = sum(warehouse.mapped('inventory_quantity_auto_apply'))
                    # print(34567, value)
