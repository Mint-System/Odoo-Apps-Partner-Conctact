import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"

    association_id = fields.Many2one("res.association")
