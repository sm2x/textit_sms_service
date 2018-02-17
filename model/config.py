# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SMS_Config(models.TransientModel):
    _inherit = 'base.config.settings'

    textit_url = fields.Char()

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