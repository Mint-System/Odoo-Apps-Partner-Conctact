import logging

from odoo import models
from odoo.osv import expression

_logger = logging.getLogger(__name__)


class Parnter(models.Model):
    _inherit = "res.partner"

    def action_show_email_history(self):
        action = self.env.ref("mail.action_view_mail_message")
        result = action.read()[0]
        subtype_id = self.env.ref("mail.mt_comment")
        result["domain"] = expression.AND(
            [
                [("subtype_id", "=", subtype_id.id)],
                expression.OR(
                    [
                        [("email_from", "ilike", self.email)],
                        [("partner_ids", "=", self.email)],
                    ]
                ),
            ]
        )
        return result
