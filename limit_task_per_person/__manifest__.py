{
    'name': 'Limit number of open tasks per user',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','project'],
    'data': [
        'views/res_users_view.xml',
    ],

    'application': False,
    'installable': True,
    'auto_install': False,
}
