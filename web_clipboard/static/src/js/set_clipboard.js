"use strict";
/**
 * Copyright 2018 Modoolar <info@modoolar.com>
 * License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).
 *
 */

odoo.define('web_clipboard.set_clipboard', function () {
    return function (value) {
        if (navigator.clipboard && window.isSecureContext) {
            // Use the Clipboard API if available
            navigator.clipboard.writeText(value).catch(err => {
                console.error('Failed to copy: ', err);
            });
        } else {
            // Fallback to the execCommand method
            const tempInput = document.createElement("input");
            tempInput.style = "position: absolute; left: -1000px; top: -1000px";
            tempInput.value = value;
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand("copy");
            document.body.removeChild(tempInput);
        }
    };
    };

});
