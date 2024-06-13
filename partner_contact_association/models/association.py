import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Association(models.Model):
    _name = "res.association"
    _description = "Association"

    name = fields.Char()
