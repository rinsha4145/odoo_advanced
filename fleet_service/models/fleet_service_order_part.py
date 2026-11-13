from odoo import api, fields, models, tools


class FleetServiceOrderPart(models.Model):
    _name = "fleet.service.order.part"
    _description = "Fleet Service Order Part"

    order_id = fields.Many2one('fleet.service.order',string="Fleet Service Order")
    product_id = fields.Many2one('product.product',string="Fleet Service Product")
    quantity = fields.Float(string="Quantity")
    unit_price = fields.Float(string="Unit Price")
