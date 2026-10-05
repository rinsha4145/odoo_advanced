{
    'name': 'Partial Delivery Control with Approval',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','product','stock'],
    'data': [
    'security/partial_delivery_control_groups.xml',
    'views/product_template_view.xml',
    'views/stock_picking_view.xml',
    'views/res_config_settings_view.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
