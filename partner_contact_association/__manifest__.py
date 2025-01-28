{
    "name": "Partner Contact Association",
    "summary": """
        Manage associtaions and assign contacts.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch",
    "category": "Administration",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner.xml",
        "views/association.xml",
    ],
    "demo": ["demo/association_demo.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
