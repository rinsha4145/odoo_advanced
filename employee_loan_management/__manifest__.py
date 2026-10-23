{
    'name': 'Employee Loan Management',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','mail', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_loan_menu.xml',
        'views/employee_loan_view.xml',
        'views/employee_installment_view.xml',
        'views/hr_employee_view.xml',

    ],
    'application': True,
    'installable': True,
    'auto_install': True,
}
