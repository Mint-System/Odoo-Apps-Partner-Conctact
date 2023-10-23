import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class Country(models.Model):
    _inherit = "res.country"
    _order = "sequence"

    sequence = fields.Integer(default=1)

    @api.model
    def reset_sequence(self):
        countries = self.env["res.country"].search([])
        countries_sorted = countries.sorted("name")
        sequence = 1
        for country in countries_sorted:
            country.write({'sequence': sequence})
            sequence += 1
