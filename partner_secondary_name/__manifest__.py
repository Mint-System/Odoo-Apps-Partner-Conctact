{
    'name': "Partner Secondary Name",

    'summary': """
        Add secondary name to partner.
    """,
    
    'author': 'Mint System GmbH, Odoo Community Association (OCA)',
    'website': 'https://www.mint-system.ch',
    'category': 'Administration',
    'version': '14.0.1.0.0',
    'license': 'AGPL-3',
    
    'depends': ['base'],

    'data': [
        'views/res_partner.xml',
    ],

    'installable': True,
    'application': False,
}