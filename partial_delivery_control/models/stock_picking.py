from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    state = fields.Selection(selection_add=[('to_approve', 'To Approve'), ('assigned', 'Ready')])

    def button_validate(self):
        for picking in self:
            need_approve = False
            if picking.state == 'to_approve' and self.env.user.has_group('partial_delivery_control.group_delivery_approval_user'):
                return super().button_validate()
            else:
                for move in picking.move_ids:
                    if not move.product_id.allow_partial_delivery:
                        if move.product_uom_qty != move.quantity:
                            need_approve = True
                            break
                if not need_approve:
                    return super().button_validate()
                else:
                    picking.write({
                        'state': 'to_approve'
                    })


    def action_approve(self):
        """approve the Delivery"""
        self.ensure_one()
        res = self.button_validate()
        return res

    def action_reject(self):
        """reject the Delivery"""
        self.state = 'draft'
