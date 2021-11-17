{
    'name': "Partner Contact Location in Name",

    'summary': """
        Zip and city in display name of contacts.
    """,
    
    'author': 'Mint System GmbH, Odoo Community Association (OCA)',
    'website': 'https://www.mint-system.ch',
    'category': 'Base',
    'version': '14.0.0.0.0',
    'license': 'AGPL-3',
    
    'depends': ['base'],

    'data': [
        'views/res_partner_view.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}