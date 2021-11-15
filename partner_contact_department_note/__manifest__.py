{
    'name': "Partner Contact Department Note",

    'summary': """
        Set departments on contacts.
    """,
    
    'author': 'Mint System GmbH, Odoo Community Association (OCA)',
    'website': 'https://www.mint-system.ch',
    'category': 'Customer Relationship Management',
    'version': '14.0.2.0.0',
    'license': 'AGPL-3',
    
    'depends': ['contacts'],

    'data': [
        'views/res_partner_view.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}