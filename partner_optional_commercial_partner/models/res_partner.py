import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_commercial_partner = fields.Boolean(
        compute="_compute_is_commercial_partner", store=True, readonly=False
    )

    @api.depends("is_company", "parent_id", "write_uid")
    def _compute_is_commercial_partner(self):
        for partner in self:
            if partner.is_company or not partner.parent_id:
                partner.is_commercial_partner = True
            elif not partner.write_uid:
                partner.is_commercial_partner = False

    @api.depends(
        "is_company", "parent_id.commercial_partner_id", "is_commercial_partner"
    )
    def _compute_commercial_partner(self):
        super()._compute_commercial_partner()
        for partner in self:
            if partner.is_commercial_partner:
                partner.commercial_partner_id = partner
