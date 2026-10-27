{
    'name': 'product owner in POS',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','product','point_of_sale'],
    'data': [
        'views/product_view.xml'
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'product_owner_in_pos/static/src/xml/orderline.js',
            'product_owner_in_pos/static/src/xml/orderline.xml',
            ]
    },
    'application': False,
    'installable': True,
    'auto_install': False,
}
