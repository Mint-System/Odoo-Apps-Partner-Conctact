from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    street2 = fields.Text()