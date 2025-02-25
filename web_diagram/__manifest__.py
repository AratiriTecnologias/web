# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).
{
    'name': 'Odoo Web Diagram',
    'category': 'Hidden',
    'description': """
Odoo Web Diagram view.
=========================

""",
    "author": "Luis Valdes",
    "website": "https://www.aratiri.cloud",
    "category": "Tools",
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "images": ["static/description/banner.png"],
    "depends": [
        "web",
    ],
    "data": [
        "views/web_diagram.xml",
    ],    
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'assets': { # https://www.odoo.com/documentation/12.0/developer/reference/javascript_reference.html#main-bundles
        'web.assets_frontend': [
            "static/src/css/base_diagram.css",
            'static/src/js/raphael.js',
            "static/lib/js/jquery.mousewheel.js",
            "static/src/js/vec2.js",
            "static/src/js/graph.js",
            "static/src/js/diagram.js",
        ],
    },
}
