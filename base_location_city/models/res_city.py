from odoo import fields, models


class ResCity(models.Model):
    _inherit = "res.city"

    latitude = fields.Float(string="Latitude", digits=(16, 13))
    longitude = fields.Float(string="Longitude", digits=(16, 13))
