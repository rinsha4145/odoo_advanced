from odoo import models, fields, api
from odoo.exceptions import ValidationError
import math


class ProjectTask(models.Model):
    _inherit = "project.task"

    hours_per_day = fields.Float(string=" Hours Per Day", tracking=True)

    @api.constrains('timesheet_ids')
    def _check_hours_per_day(self):
        """limit the hours per day for the timesheets in a task"""
        for task in self:
            print(45678, task.hours_per_day)
            latest_line = task.timesheet_ids.search([], order='write_date desc', limit=1)
            print(111, latest_line.date)

            for timesheet in task.timesheet_ids:
                timesheets = self.env['account.analytic.line'].search(
                    [('task_id', '=', task.id), ('date', '=', timesheet.date)])
                sum_of_time = sum(timesheets.mapped('unit_amount'))
                print(7979, sum_of_time)
                if latest_line.date == timesheet.date and sum_of_time > task.hours_per_day:
                    raise ValidationError(
                        "The hour limit for the day %s has been exceeded." % timesheet.date)
