{
    "name": "Partner Multi Pricelist",
    "summary": """
        Assign mutliple pricelists with start and end date to customers.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Sales",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["sale"],
    "data": ["security/ir.model.access.csv", "views/partner.xml", "views/sale.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
