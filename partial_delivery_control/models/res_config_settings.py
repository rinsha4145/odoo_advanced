from odoo import fields, models,api,Command
from odoo.tools import ormcache


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    approval_users = fields.Many2many(related='company_id.approval_users',readonly=False)

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        approval_group = self.env.ref('partial_delivery_control.group_delivery_approval_user',False)
        print(approval_group)
        for user in self.approval_users:
            user.write({
                'group_ids': [Command.link(approval_group.id)]
            })
        users_to_remove = approval_group.user_ids - self.approval_users
        for user in users_to_remove:
            user.write({
                 'group_ids': [Command.unlink(approval_group.id)]
            })