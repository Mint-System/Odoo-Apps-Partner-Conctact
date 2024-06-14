import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

from odoo.osv import expression


class Partner(models.Model):
    _inherit = "res.partner"

    association_id = fields.Many2one("res.association")
    association_name = fields.Char(
        related="association_id.name", string="Assocation Name", store=True
    )

    def _get_name(self):
        """Show association name is displayname."""
        partner = self
        name = super(Partner, self)._get_name()
        if partner.association_id:
            name = "%s, %s" % (partner.association_id.name, name)
        return name

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        """Always search in association name."""
        if args is None:
            args = []
        args = expression.OR([args, [("association_name", operator, name)]])
        _logger.warning(args)
        return super().name_search(name=name, args=args, operator=operator, limit=limit)
