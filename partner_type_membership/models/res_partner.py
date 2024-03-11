import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    type = fields.Selection(
        selection_add=[("membership", "Membership Contact Address")],
        ondelete={"membership": "set default"},
    )

    def get_address_default_type(self):
        """Add new order type."""
        res = super().get_address_default_type()
        res.add("membership")
        return res

    def _get_name(self):
        partner = self
        name = super(ResPartner, self)._get_name()
        if partner.company_name or partner.parent_id:
            if not partner.name and partner.type in ["membership"]:
                name += (
                    " "
                    + dict(self.fields_get(["type"])["type"]["selection"])[partner.type]
                )
        return name

    def _avatar_get_placeholder_path(self):
        if self.type == "membership":
            return "partner_type_membership/static/img/membership.png"
        return super()._avatar_get_placeholder_path()
