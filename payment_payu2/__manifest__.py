{
    'name': 'PayU2 Payment',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','payment'],
    'data': [
        'views/payment_provider_views.xml',
        'views/payment_payu_templates.xml',
        'data/payment_provider_data.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
