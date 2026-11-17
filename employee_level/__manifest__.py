{
    'name': 'Employee Level',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_level_view.xml',
        'views/hr_employee_view.xml',

    ],

    'application': False,
    'installable': True,
    'auto_install': False,
}
