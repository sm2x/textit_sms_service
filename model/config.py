# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SMS_Config(models.TransientModel):
    _inherit = 'base.config.settings'

    url = fields.Char()

    @api.multi
    def set_sms_api_url(self):
        url = self[0].url or ''
        self.env['ir.config_parameter'].set_param('url', url)

    @api.multi
    def get_default_sms_credentials(self, fields=None):
        get_param = self.env['ir.config_parameter'].get_param
        url = get_param('url', default='')
        return {
            'url' : url
        }