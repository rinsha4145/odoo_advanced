{
    'name': 'Bill of Material in Cart',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','product','website_sale'],
    'data': [
        'views/res_config_settings_view.xml',
        'views/cart_template.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
