from odoo import api, fields, models, tools
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    picking_ids = fields.One2many(
        'stock.picking', 'invoice_id', string='Pickings')
    delivery_count = fields.Integer(string='Delivery Orders', compute='_compute_picking_ids')

    def action_post(self):
        """inherit the action of confirm a invoice from there create a delivery if it has no sale order"""
        for move in self:
            if move.invoice_origin == False:
                if move.move_type != 'out_invoice':
                    raise UserError('Delivery Orders only created in invoice')
                else:
                    warehouse = move.env['stock.warehouse'].search([('company_id', '=', self.company_id.id)], limit=1)
                    print(7890, move.name)
                    picking_vals = {
                        'picking_type_id': warehouse.out_type_id.id,
                        'location_id': warehouse.lot_stock_id.id,
                        'location_dest_id': move.partner_id.property_stock_customer.id,
                        'partner_id': move.partner_id.id,
                        'origin': move.name,
                        'move_type': 'direct',
                        'invoice_id': move.id,
                        # 'date_deadline': self.invoice_due_date
                    }
                    picking = move.env['stock.picking'].create(picking_vals)
                    for line in move.invoice_line_ids:
                        print(456789, picking.location_dest_id)
                        if line.product_id.type == 'consu':
                            move_vals = {
                                'product_id': line.product_id.id,
                                'product_uom_qty': line.quantity,
                                'picking_id': picking.id,
                                'location_final_id': picking.location_dest_id.id,

                            }
                            self.env['stock.move'].create(move_vals)
        return super().action_post()

    @api.depends('picking_ids')
    def _compute_picking_ids(self):
        for order in self:
            order.delivery_count = len(order.picking_ids)

    def action_view_delivery(self):
        if self.invoice_origin == False:
            print(34938)
            return self._get_action_view_picking(self.picking_ids)

    def _get_action_view_picking(self, pickings):
        '''
        This function returns an action that display existing delivery orders
        of given sales order ids. It can either be a in a list or in a form
        view, if there is only one delivery order to show.
        '''
        print(22222222222)
        action = self.env["ir.actions.actions"]._for_xml_id("stock.action_picking_tree_all")

        if len(pickings) > 1:
            action['domain'] = [('id', 'in', pickings.ids)]
        elif pickings:
            form_view = [(self.env.ref('stock.view_picking_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state, view) for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = pickings.id
        # Prepare the context.
        picking_id = pickings.filtered(lambda l: l.picking_type_id.code == 'outgoing')
        if picking_id:
            picking_id = picking_id[0]
        else:
            picking_id = pickings[0]
        action['context'] = dict(
            default_partner_id=self.partner_id.id,
            default_picking_type_id=picking_id.picking_type_id.id,
        )
        return action
