from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_amount = fields.Float(string="Discount Amount", compute="_compute_discount_amount",default=0.0)
    state = fields.Selection(selection_add=[('to approve', 'To Approve'), ('sale', "Sales Order")])

    @api.depends('order_line.price_unit', 'order_line.discount', 'order_line.product_uom_qty')
    def _compute_discount_amount(self):
        """sum the total discount amount"""
        for record in self:
            for line in record.order_line:
                if line.discount > 0:
                    record.discount_amount += line.price_unit * line.product_uom_qty * line.discount / 100


    def action_confirm(self):
        """confirm the order check the discount amount"""
        if self.env.user.has_group('sales_team.group_sale_manager'):
            print(self.env.user.has_group('sales_team.group_sale_manager'))
            return super().action_confirm()
        else:
            orders_to_confirm = self.env['sale.order']
            print(orders_to_confirm)
            for record in self:
                # param_value = self.env['ir.config_parameter'].sudo().get_param(
                # 'discount_approval.so_double_validation_amount') or False
                # settings_discount_value = float(param_value) if param_value else 0.0
                settings_discount_value = record.company_id.so_double_validation_amount
                settings_discount_approve = record.company_id.so_order_approval
                # settings_discount_approve = self.env['ir.config_parameter'].sudo().get_param('discount_approval.so_order_approval') or False
                va=record.read(['name','state','discount_amount'])
                print(va)
                if record.discount_amount > settings_discount_value and settings_discount_approve:
                    print(record.name)
                    print(record.discount_amount)
                    record.state = 'to approve'
                else:
                    orders_to_confirm |= record
            if orders_to_confirm :
                return super(SaleOrder,orders_to_confirm).action_confirm()
            return True

    def action_approve(self):
        """approve the order"""
        self.state = 'draft'
        return super().action_confirm()

    def action_reject(self):
        """reject the sale order"""
        self.state = 'draft'
        self.message_post(body=("Sale Order Rejected By %s")
                               % (self.env.user.name),
                          message_type="comment",
                          subtype_xmlid="mail.mt_comment")
