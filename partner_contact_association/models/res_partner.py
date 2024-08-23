import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"
    _rec_names_search = [
        "display_name",
        "email",
        "ref",
        "vat",
        "company_registry",
        "association_name",
    ]

    association_id = fields.Many2one("res.association")
    association_name = fields.Char(
        related="association_id.name", string="Assocation Name", store=True
    )

    def _compute_display_name(self):
        super()._compute_display_name()
        for rec in self:
            if rec.association_id:
                rec.display_name = "{} ({})".format(rec.name, rec.association_id.name)
