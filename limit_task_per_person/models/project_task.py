from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.constrains('user_ids')
    def limit_the_task(self):
        print(56789)
        for user in self.user_ids:
            limit = user.task_limit
            if limit > 0:
                print(456, user.read())
                assigned_tasks = self.env['project.task'].search_count(
                    [('user_ids', 'in', [user.id]), ('state', 'not in', ['1_done', '1_canceled'])])

                print(34567, assigned_tasks)
                if assigned_tasks > limit:
                    raise ValidationError('%s have task limit of %s' % (user.display_name, limit))
