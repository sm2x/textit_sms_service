# -*- coding: utf-8 -*-

import requests,time

import logging
from odoo import models, fields, api,_
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class SMS_Template(models.TransientModel):
    _name = 'sms.templates'
    
    to = fields.Char()
    message = fields.Text()

    @api.onchange('to')
    def onload(self):
        numbers = ''
        active_class =self.env['res.partner'].browse(self._context.get('active_ids'))
        if len(active_class) > 1:
            for rec in active_class:
                if rec.mobile != False:
                    numbers = numbers + rec.mobile + ','
        else:
            numbers = numbers + active_class.mobile
        self.to = numbers

    @api.constrains('message')
    def message_check(self):
        if not self.message:
            raise ValidationError(_('You should have to type some message..'))

    @api.multi
    def send(self):
        get_param = self.env['ir.config_parameter'].get_param
        number = self.to
        message = self.message
        message = message.replace(" ", "%20")
        textit_url = get_param('textit_url', default='')

        if textit_url != '':

            if not ',' in number:
                _logger.info(">>>> Sendings sms to number : %s" %(number))
                try:
                    send_sms(number,message)
                    _logger.info('>>>>>Message sent')
                except Exception as e:
                    raise ValidationError(_('Facing error something like : [%s]' %(e)))
            else:
                bulk_numbers = number.split(',')
                for number in bulk_numbers[:-1]:
                    _logger.info(">>>> Sendings sms to number : %s" %(x))
                    try:
                        send_sms(number,message)
                        _logger.info('>>>>>Message sent')
                        time.sleep( 5 )
                    except Exception as e:
                        raise ValidationError(_('Facing error something like : [%s]' %(e)))
        else:
            raise ValidationError(_('You should have to assign textit api first at General Settings'))

    def send_sms(number,message):
        headers = {
                'Authorization': 'Token 45855a8fdf2280817fd1a0649f57169271c8d621',
                'Content-Type': 'application/json'
            }
        data = '{"urns": ["tel:%s"],"text": "%s"}' %(number,message)
        _logger.info('Sending message : '+message+' on Number : '+number)
        rec = requests.post(textit_url, headers=headers, data=data)