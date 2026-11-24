{
    'name': 'Invetory Dashboard',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base', 'stock', 'product', 'stock'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/dashboard_view.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'inventory_dashboard/static/css/dashboard_cards.css',

        ],
        'web.assets_backend': [
            'inventory_dashboard/static/src/js/dashboard.js',
            'inventory_dashboard/static/src/xml/dashboard_template.xml',
            'inventory_dashboard/static/src/xml/dashboard_cards.xml',
            'inventory_dashboard/static/src/xml/warehouse_info_table.xml',
            'inventory_dashboard/static/src/xml/location_stock_info.xml',
            'inventory_dashboard/static/src/xml/filtering.xml',
        ],

    },
    'application': False,
    'installable': True,
    'auto_install': False,
}
