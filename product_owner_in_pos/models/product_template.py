from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    owner_id = fields.Many2one('product.owner', string="Owner")

    @api.model
    def _load_pos_data_fields(self, config_id):
        """Return fields to be loaded into the POS."""
        data = super()._load_pos_data_fields(config_id)
        data.append('owner_id')
        print(12345,data)
        return data