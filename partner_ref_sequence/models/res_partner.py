from odoo import api, models
import logging
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('res.partner.ref')
        return super().create(vals)
