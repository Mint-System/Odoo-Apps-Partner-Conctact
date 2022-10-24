import logging
from odoo import _, api, fields, models
_logger = logging.getLogger(__name__)


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'
    
    _sql_constraints = [
        ('unique_number', 'check(1, 1)', 'Account Number must be unique'),
    ]