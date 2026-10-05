from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    state = fields.Selection(selection_add=[('to_approve', 'To Approve'), ('assigned', 'Ready')])

    def button_validate(self):
        for picking in self:
            need_approve = False
            for move in picking.move_ids:
                if not move.product_id.allow_partial_delivery:
                    if move.product_uom_qty != move.quantity:
                        picking.write({
                            'state': 'to_approve'
                        })
                        print(picking.state)
                        need_approve = True
                        break
        if not need_approve:
            return super().button_validate()

    def action_approve(self):
        """approve the Delivery"""
        self.ensure_one()
        print(self.name)
        # self.state = 'assigned'
        return super().button_validate()

    def action_reject(self):
        """reject the Delivery"""
        self.state = 'draft'
