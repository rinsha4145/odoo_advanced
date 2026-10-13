from odoo import api, fields, models, tools


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    restrict_user_ids = fields.Many2many(
        'res.users', string="Restricted Users",
        help='Users restricted from accessing this menu.')

    @api.model
    def _filter_visible_menus(self):
        """filter the menu for the visibility"""
        print(936835)
        menus = super()._filter_visible_menus()
        print(77777)
        return menus.filtered(
            lambda m: self.env.user not in m.restrict_user_ids)
