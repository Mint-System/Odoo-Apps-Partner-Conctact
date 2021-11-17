from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"

    def name_get(self):
        _logger.warning(self)
        # Append zip and city if context is given
        if self.env.context.get('show_zip_and_city'):
            recs = super(Partner, self).name_get()
            _logger.warning(recs)
            for rec in recs:
                if rec.zip:
                    rec.name += ', ' + rec.zip
                if rec.city:
                    rec.name += ' ' + rec.city
        else:
            result = super(Partner, self).name_get()
        return result
