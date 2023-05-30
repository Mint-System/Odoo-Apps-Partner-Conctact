from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = 'res.users'

    private_street2 = fields.Text()