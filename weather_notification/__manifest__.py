{
    'name': 'Weather Notification',
    'version': '19.0.1.1',
    'author': 'Rinsha',
    'website': 'https://www.yourwebsite.com',
    'sequence': -10,
    'license': 'LGPL-3',
    'depends': ['base','web','mail'],
    'data': [
        'security/ir.model.access.csv',

    ],
    'assets': {

       'web.assets_backend': [
           'weather_notification/static/src/xml/weather_icon.xml',
           'weather_notification/static/src/js/weather_icon.js',
        ],
    },
    'application': False,
    'installable': True,
    'auto_install': False,
}
