import logging

from odoo import models
from odoo.osv import expression

_logger = logging.getLogger(__name__)


class Parnter(models.Model):
    _inherit = "res.partner"

    def action_show_email_history(self):
        action = self.env.ref("mail.action_view_mail_mail")
        result = action.read()[0]
        domain = expression.OR(
            [
                [("email_from", "ilike", self.email)],
                [("email_to", "=", self.email)],
                [("recipient_ids", "=", self.email)],
            ]
        )
        result["domain"] = domain
        return result
