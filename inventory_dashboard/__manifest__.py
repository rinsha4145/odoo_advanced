{
    'name': 'Invetory Dashboard',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','stock','product','stock'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/dashboard_view.xml'
    ],
    'assets': {

       'web.assets_backend': [
           'inventory_dashboard/static/src/js/dashboard.js',
          'inventory_dashboard/static/src/xml/dashboard_template.xml'
        ],
    },
    'application': False,
    'installable': True,
    'auto_install': False,
}
