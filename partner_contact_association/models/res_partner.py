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

    def _compute_display_name(self):
        super()._compute_display_name()
        for rec in self:
            if rec.association_id:
                rec.display_name = "{} ({})".format(
                    rec.name, rec.association_id.name
                )
    
    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        """Always search in association name."""
        if args is None:
            args = []
        args = expression.OR([args, [("association_name", operator, name)]])
        _logger.warning(args)
        return super().name_search(name=name, args=args, operator=operator, limit=limit)
