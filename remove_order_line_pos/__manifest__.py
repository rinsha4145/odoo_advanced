{
    'name': 'Remove order line in POS',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base', 'point_of_sale'],
    'data': [

    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'remove_order_line_pos/static/src/xml/orderline.js',
            'remove_order_line_pos/static/src/xml/orderline.xml',
            'remove_order_line_pos/static/src/xml/order_display.js',
            'remove_order_line_pos/static/src/xml/order_display.xml',
        ],
    },
    'application': False,
    'installable': True,
    'auto_install': False,
}
