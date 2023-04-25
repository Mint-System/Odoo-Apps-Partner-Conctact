from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = 'res.partner'

    partner_pricelist_ids = fields.One2many('partner.pricelist', 'partner_id')

    @api.depends('partner_pricelist_ids.pricelist_id', 'partner_pricelist_ids.sequence')
    def _compute_product_pricelist(self):
        """Filter partner pricelists by sequence and date."""
        super()._compute_product_pricelist()

        # Read filter date from context
        date = self._context.get('date') or fields.Datetime.now()
        # _logger.warning(['_compute_product_pricelist', date])
        
        for partner in self:
            pricelist_ids = partner.partner_pricelist_ids

            if pricelist_ids:
                partner.property_product_pricelist = pricelist_ids[0].pricelist_id.id
            
                # Get and set pricelist filtered by date                
                filtered_pricelist = pricelist_ids.filtered(lambda l:
                    (l.date_start and l.date_end and (l.date_start <= date <= l.date_end)) or
                    (l.date_start and not l.date_end and l.date_start <= date) or
                    (l.date_end and not l.date_start and date <= l.date_end)
                )
                if filtered_pricelist:
                    partner.property_product_pricelist = filtered_pricelist[0].pricelist_id.id
