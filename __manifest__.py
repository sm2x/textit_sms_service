# -*- coding: utf-8 -*-
{
    'name': "Textit SMS Services",

    'summary': """
        Send Single and Bulk SMS to Targets using textit.in""",
    'description': """
        Go to "textit.in".Check there pricing.After signup copy
        authentication token. 
        In odoo go to General Settings .In "SMS Setting" past Token.
        Then you can send sms whenever you want with the hlep of
        below code:

        from odoo.addons.textit_sms_service import sms as send
        send.sms(number,message)

    """,
    'author': "Wahab Ali Malik",
    'website': "http://www.datagenie.com",
    'version': '0.1',
    'depends': ['base','mail','contacts'],
    'data': [
        'security/sms_activation_group.xml',
        'views/config.xml',
        'views/sms_template.xml',
    ],
}