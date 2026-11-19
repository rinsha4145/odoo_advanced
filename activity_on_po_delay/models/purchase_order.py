from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.depends('picking_ids', 'picking_ids.state')
    def _compute_receipt_status(self):
        super()._compute_receipt_status()
        for order in self:
            if order.receipt_status == 'full':

                exist = order.env['mail.activity'].search(
                    [('res_id', '=', order.id), ('summary', '=', 'delay of delivery')])
                if exist:
                    # exist.write({'date_done':fields.Date.today(),'active':False})
                    exist._action_done()

                    # thread = this.env.services["mail.store"].Thread.insert({
                    #     model: res_model,
                    #     id: res_id,
                    # });
                    print(231234, exist.read())

    def cron_activity(self):
        purchase_order = self.env["purchase.order"].search([("state", "=", "purchase")])
        for purchase in purchase_order:
            transfers = self.env['stock.picking'].search(
                ['&', ("state", "not in", ["done", "cancel"]), ("picking_type_code", "=", "incoming"),
                 ('purchase_id', '=', purchase.id), ('date_deadline', '<', fields.Datetime.now())])
            for picking in transfers:
                if picking:
                    exist = self.env['mail.activity'].search(
                        [('res_id', '=', purchase.id), ('summary', '=', 'delay of delivery')])
                    if not exist:
                        self.env['mail.activity'].create({
                            'res_id': purchase.id,
                            'res_model_id': self.env['ir.model']._get_id('purchase.order'),
                            'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id,
                            'summary': 'delay of delivery',
                            'note': 'the product have not received.',
                            'res_name': purchase.name,
                            'date_deadline': fields.Date.today(),
                            'user_id': purchase.user_id.id,
                        })

                    manager = self.env.ref('purchase.group_purchase_manager')

                    for user in manager.user_ids:
                        mail_values = {
                            'subject': 'Delivery of Purchase Order',
                            'body_html': '<p>The Purchase order ' + purchase.name + ' delivery has been delayed</p>',
                            'email_from': self.env.company.email,
                            'email_to': user.email,
                            'model': self._name,
                            'res_id': self.id,
                        }
                        self.env['mail.mail'].sudo().create(mail_values).send()
