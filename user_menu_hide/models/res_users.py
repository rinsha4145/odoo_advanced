from odoo import api, fields, models, tools,Command
class ResUsers(models.Model):
    _inherit = 'res.users'

    menu_ids = fields.Many2many('ir.ui.menu',string='Menus')

    def write(self, vals):
        res = super().write(vals)
        print(res)
        print(3456789,vals)
        print(4567,self.menu_ids)
        if 'menu_ids' in vals:
            for menu in self.menu_ids:
                menu.write({'restrict_user_ids': [Command.link(self.id)]})
                print(1298)
        self.menu_ids._filter_visible_menus()
        return res
