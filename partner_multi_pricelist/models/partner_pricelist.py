from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PartnerPricelist(models.Model):
    _name = 'partner.pricelist'
    _description = 'Partner Pricelist'
    _order = "sequence asc, id desc"

    sequence = fields.Integer()
    partner_id = fields.Many2one('res.partner', 'Customer')
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist')
    date_start = fields.Datetime('Start Date')
    date_end = fields.Datetime('End Date')