from odoo import api, fields, models, tools

class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    restrict_user_ids = fields.Many2many(
        'res.users', string="Restricted Users",
        help='Users restricted from accessing this menu.')


    def _filter_visible_menus(self):
        """
        Override to filter out menus restricted for current user.
        Applies only to the current user context.
        """
        menus = super()._filter_visible_menus()

        # Allow system admin to see everything
        if self.env.user.has_group('base.group_system'):
            return menus
        print(77777)
        return menus.filtered(
            lambda m: self.env.user not in m.restrict_user_ids)