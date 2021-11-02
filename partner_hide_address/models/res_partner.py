from odoo import api, models, fields
import logging
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    hide_address = fields.Boolean()
