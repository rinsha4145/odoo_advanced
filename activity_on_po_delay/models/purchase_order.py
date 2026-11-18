from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def cron_activity(self):
        purchase_order = self.env["purchase.order"].search([("state", "=", "purchase")])
        for purchase in purchase_order:
            transfers = self.env['stock.picking'].search(
                ['&', ("state", "not in", ["done", "cancel"]), ("picking_type_code", "=", "incoming"),
                 ('purchase_id', '=', purchase.id)])
            for picking in transfers:
                if picking.date_deadline and picking.date_deadline < fields.Datetime.now():
                    exist = self.env['mail.activity'].search([('res_id','=',purchase.id),('summary','=','delay of delivery')])
                    if not exist:
                        print(890,purchase.id)
                        self.env['mail.activity'].create({
                            'res_id': purchase.id,
                            'res_model_id': self.env['ir.model']._get_id('purchase.order'),
                            'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id,
                            'summary': 'delay of delivery',
                            'note': 'the product have not received.',
                            'res_name':purchase.name,
                            'date_deadline': fields.Date.today(),
                            'user_id': purchase.user_id.id,
                        })

                    manager = self.env.ref('purchase.group_purchase_manager')
                    print(56789, manager)

                    for user in manager.user_ids:
                        print(1234,purchase.read())
                        mail_values = {
                            'subject': 'Delivery of Purchase Order',
                            'body_html': '<p>The Purchase order ' + purchase.name + ' delivery has been delayed</p>',
                            'email_from': self.env.company.email,
                            'email_to': user.email,
                            'model': self._name,
                            'res_id': self.id,
                        }
                        print(1234, mail_values)
                        self.env['mail.mail'].sudo().create(mail_values).send()
