from odoo import api, fields, models
class ResUsers(models.Model):
    _inherit = 'res.users'

    purchase_order_ids = fields.Many2many('purchase.order',string='Purchase Orders',compute="_compute_partner_id")
    product_ids = fields.Many2many('product.product',string='Products',compute="_compute_product_ids")
    product_count = fields.Integer(string='Product Count')


    @api.depends('partner_id')
    def _compute_partner_id(self):
        for purchase_order in self:
            if purchase_order.partner_id:
                purchase_order.purchase_order_ids = self.env['purchase.order'].search([
                    ('partner_id', '=', purchase_order.partner_id.id)
                ])
            else:
                purchase_order.purchase_order_ids = False

    @api.depends('purchase_order_ids')
    def _compute_product_ids(self):
        self.product_ids = self.purchase_order_ids.order_line.product_id
        print(4567,len(self.product_ids))
        self.product_count = len(self.product_ids)

    def action_get_product_records(self):
        """GET Product RECORDS FOR SMART BUTTON"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Products',
            'view_mode': 'list',
            'res_model': 'product.product',
            'domain': [('id', 'in', self.product_ids.ids)],
            'context': "{'create': False}"
        }


