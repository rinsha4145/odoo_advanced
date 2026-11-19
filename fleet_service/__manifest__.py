{
    'name': 'fleettt service',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','product','hr','fleet'],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_service_order_view.xml',
        'views/fleet_vehicle_view.xml',
        'views/hr_employee_view.xml',
        'views/fleet_service_menu.xml',


    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
