{
    'name': 'Automated Purchase Order',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','product'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/product_wizard.xml',
        'views/product_views.xml',

    ],

    'application': False,
    'installable': True,
    'auto_install': False,
}
