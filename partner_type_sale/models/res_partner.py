from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(selection_add=[
        ('sale', 'Sale Contact Address')
    ], ondelete={'sale': 'set default'})

    def get_address_default_type(self):
        """Add new order type."""
        res = super().get_address_default_type()
        res.add('sale')
        return res

    def _get_name(self):
        partner = self
        name = super(ResPartner, self)._get_name()
        if partner.company_name or partner.parent_id:
            if not partner.name and partner.type in ['sale']:
                name += dict(self.fields_get(['type'])['type']['selection'])[partner.type]
        return name