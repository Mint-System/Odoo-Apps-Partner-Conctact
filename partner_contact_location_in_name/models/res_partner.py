from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"

    def name_get(self):
        res = []
        # Append zip and city if context is given
        if self.env.context.get('show_zip_and_city'):
            
            for partner in self:
                name = partner.display_name
                if partner.zip:
                    name += ', ' + partner.zip
                if partner.city:
                    name += ' ' + partner.city
                res.append((partner.id, name))
        else:
            res = super(Partner, self).name_get()
        return res
