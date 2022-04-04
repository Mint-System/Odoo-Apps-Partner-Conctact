{
    'name': "Partner Hide Address",

    'summary': """
        Option to hide address on reports. 
    """,
    
    'author': 'Mint System GmbH, Odoo Community Association (OCA)',
    'website': 'https://www.mint-system.ch',
    'category': 'Sale',
    'version': '14.0.1.0.0',
    'license': 'AGPL-3',
    
    'depends': ['base'],

    'data': [
        'views/res_partner.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
    "images": ["images/screen.png"],
}