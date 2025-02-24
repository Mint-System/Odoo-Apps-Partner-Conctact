import logging

from odoo import models

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"

    def action_show_email_history(self):
        action = self.env.ref("mail.action_view_mail_message").read()[0]
        subtype_id = self.env.ref("mail.mt_comment")
        message_type = "email"
        action["domain"] = [
            "&",
            "|",
            ("subtype_id", "=", subtype_id.id),
            ("message_type", "=", message_type),
            "|",
            ("author_id", "ilike", self.email),
            "|",
            ("email_from", "ilike", self.email),
            ("partner_ids", "ilike", self.email),
        ]
        return action
