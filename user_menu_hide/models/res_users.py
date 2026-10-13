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
            for user in self:
                old_menus = self.env['ir.ui.menu'].search([('restrict_user_ids','in',user.id)])
                old_menus.write({'restrict_user_ids': [Command.link(user.id)]})
        return res
