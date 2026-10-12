from odoo import api, fields, models, tools
class ResUsers(models.Model):
    _inherit = 'res.users'

    menu_ids = fields.Many2many('ir.ui.menu',string='Menus')

    @api.onchange('menu_ids')
    def _onchange_ids(self):
        if self.menu_ids:
            self.menu_ids.restrict_user_ids = self.ids
        print(34567,self.menu_ids.restrict_user_ids)
        self.menu_ids._filter_visible_menus()

