# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class SMS_Config(models.TransientModel):
    _inherit = 'base.config.settings'

    group_sms_activation = fields.Selection([
        (0, 'Unactive SMS'),
        (1, 'Activate SMS')
        ], "Killbill ID",
        implied_group='textit_sms_service.group_sms_form'
        )

    textit_url = fields.Char("Textit URL")

    @api.multi
    def set_sms_api_textit_url(self):
        textit_url = self[0].textit_url or ''
        self.env['ir.config_parameter'].set_param('textit_url', textit_url)

    @api.multi
    def get_default_sms_credentials(self, fields=None):
        get_param = self.env['ir.config_parameter'].get_param
        textit_url = get_param('textit_url', default='')
        return {
            'textit_url' : textit_url
        }

    def execute(self):
        if self.group_sms_activation:
            if not self.textit_url:
                raise ValidationError(_("Please fill URL of API."))
        elif not self.group_sms_activation:
            self.textit_url = False
        return super(SMS_Config, self).execute()