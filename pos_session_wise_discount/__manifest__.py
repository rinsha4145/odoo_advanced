{
    'name': 'POS Session Wise Discount',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base', 'pos_sale'],
    'data': [
        'views/res_config_settings_view.xml'
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            # 'pos_session_wise_discount/static/src/pos_store.js',
            # 'pos_session_wise_discount/static/src/payment_screen.js',
            # 'pos_session_wise_discount/static/src/control_buttons.xml',
            # 'pos_session_wise_discount/static/src/control_buttons.js'
        ]
    },
    'application': False,
    'installable': True,
    'auto_install': False,
}
