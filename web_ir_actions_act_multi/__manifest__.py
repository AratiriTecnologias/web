# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

{
    "name": "Web Actions Multi",
    "summary": "Enables triggering of more than one action on ActionManager",
    "category": "Web",
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "author": "Modoolar",
    "website": "https://www.modoolar.com/",
    "images": ["static/description/banner.png"],
    "depends": ["web"],
    "data": [
        "views/web_ir_actions_act_multi.xml",
    ],
    'assets': { # https://www.odoo.com/documentation/12.0/developer/reference/javascript_reference.html#main-bundles
        'web.assets_frontend': [
            "static/src/js/web_ir_actions_act_multi.js",
        ],
    },
    "installable": True,
}
