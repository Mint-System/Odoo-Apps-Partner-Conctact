from odoo import fields, models


class ResCityZip(models.Model):
    _inherit = "res.city.zip"

    latitude = fields.Float(digits=(16, 13))
    longitude = fields.Float(digits=(16, 13))
