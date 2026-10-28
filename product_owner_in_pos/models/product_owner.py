from odoo import api, fields, models


class ProductOwner(models.Model):
    _name = 'product.owner'
    _description = 'Product Owner'
    _inherit = ['pos.load.mixin']

    name = fields.Char(string='Name', required=True)


    @api.model
    def _load_pos_data_fields(self, config_id):
        """Return fields to be loaded into the POS."""
        print(986)
        return ['id', 'name']
