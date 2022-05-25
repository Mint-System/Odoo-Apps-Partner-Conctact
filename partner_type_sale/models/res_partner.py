from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    type = fields.Selection(selection_add=[
        ('sale', 'Sale Contact Address')
    ], ondelete={'sale': 'set default'})

    def get_address_default_type(self):
        """Add new order type"""
        res = super().get_address_default_type()
        res.add("sale")
        return res