from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    email2 = fields.Char(string="Secondary E-Mail")
