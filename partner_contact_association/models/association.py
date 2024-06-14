import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Association(models.Model):
    _name = "res.association"
    _description = "Association"

    name = fields.Char()
    member_ids = fields.One2many("res.partner", "association_id", string="Members")
    member_count = fields.Integer(compute="_compute_member_count")

    def _compute_member_count(self):
        for association in self:
            association.member_count = len(association.member_ids)

    def action_view_members(self):
        self.ensure_one()
        return {
            "name": "Members",
            "type": "ir.actions.act_window",
            "res_model": "res.partner",
            "view_mode": "tree,form",
            "domain": [("id", "in", self.member_ids.ids)],
        }
