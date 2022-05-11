from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    type = fields.Selection(selection_add=[
        ('order', 'Order Address')
    ], ondelete={'contact': 'set default'})
