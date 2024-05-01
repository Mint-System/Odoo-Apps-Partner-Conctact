from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    name2 = fields.Char(string="Secondary Name")
