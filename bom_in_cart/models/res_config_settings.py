from odoo import fields, models,api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    product_ids = fields.Many2many(related='company_id.product_ids',readonly=False)

    @api.onchange('product_ids')
    def onchange_product_ids(self):
        for record in self.product_ids:
           if record.bom_ids:
               print('yes')


