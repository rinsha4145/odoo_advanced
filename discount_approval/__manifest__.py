{
    'name': 'Discount Approval',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','sale'],
    'data': [
        'views/res_config_settings_view.xml',
        'views/sale_order_view.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
