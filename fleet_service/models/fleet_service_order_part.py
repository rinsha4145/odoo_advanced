from odoo import api, fields, models, tools


class FleetServiceOrderPart(models.Model):
    _name = "fleet.service.order.part"
    _description = "Fleet Service Order Part"

    order_id = fields.Many2one('fleet.service.order',string="Service Order")
    product_id = fields.Many2one('product.product',string="Service Product")
    quantity = fields.Float(string="Quantity")
    unit_price = fields.Float(string="Unit Price")

    @api.onchange('product_id')
    def onchange_product_id(self):
        print(789,self.product_id)
        self.unit_price = self.product_id.lst_price