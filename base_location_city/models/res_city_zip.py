from odoo import fields, models


class ResCity(models.Model):
    _inherit = "res.city"

    latitude = fields.Float(digits=(16, 13))
    longitude = fields.Float(digits=(16, 13))
