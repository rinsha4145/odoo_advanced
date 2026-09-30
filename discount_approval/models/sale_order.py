from odoo import fields, models,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_amount = fields.Float(string="Discount Amount",compute="_compute_discount_amount")
    state = fields.Selection(selection_add=[('to approve','To Approve'),('sale', "Sales Order")])
    @api.depends('order_line.price_unit','order_line.discount','order_line.product_uom_qty')
    def _compute_discount_amount(self):
        """sum the total discount amount"""
        for record in self:
            for value in self:
                for line in value.order_line:
                    if line.discount > 0:
                        record.discount_amount += line.price_unit * line.product_uom_qty * line.discount / 100
                    else:
                        continue
        print(record.discount_amount)

    def action_confirm(self):
        """confirm the order check the discount amount"""
        if self.env.user.has_group('sales_team.group_sale_manager'):
            print(888)
            print(self.env.user.has_group('sales_team.group_sale_manager'))
            return super().action_confirm()
        else:
            for record in self:
                print(678)
                # param_value = self.env['ir.config_parameter'].sudo().get_param(
                    # 'discount_approval.so_double_validation_amount') or False
                # settings_discount_value = float(param_value) if param_value else 0.0
                settings_discount_value = record.company_id.so_double_validation_amount
                print(settings_discount_value)
                settings_discount_approve = record.company_id.so_order_approval

                # settings_discount_approve = self.env['ir.config_parameter'].sudo().get_param('discount_approval.so_order_approval') or False
                print(settings_discount_approve)

                if record.discount_amount > settings_discount_value and settings_discount_approve:
                    record.state = 'to approve'
                else:
                    return super().action_confirm()
                print(23, settings_discount_value)
                print(234, settings_discount_approve)

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













