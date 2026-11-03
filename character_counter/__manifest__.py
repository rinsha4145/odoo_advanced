{
    'name': 'Character Counter Input Widget',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','sale'],
    'data': [
        'views/sale_order_view.xml'
    ],
    'assets': {
      'point_of_sale._assets_pos': [
      ],
       'web.assets_backend': [
           'character_counter/static/src/js/character_counter.js',
           'character_counter/static/src/js/character_counter.xml'
           
        ],
    },
    'application': False,
    'installable': True,
    'auto_install': False,
}
