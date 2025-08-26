{
    "name": "IP Web Theme",
    "summary": "A unified backend theme for Odoo Community Edition.",
    "description": """
        This module combines the functionality of muk_web_appsbar, muk_web_chatter,
        muk_web_colors, muk_web_dialog, and ip_web_theme into a single, cohesive theme.
    """,
    "version": "18.0.1.0.0",
    "category": "Themes/Backend",
    "license": "LGPL-3",
    "author": "MuK IT",
    "website": "http://www.mukit.at",
    "depends": [
        "base_setup",
        "web",
        "mail",
        "web_editor",
    ],
    "data": [
        "templates/web_layout.xml",
        "templates/webclient.xml",
        "views/res_config_settings.xml",
        "views/res_users.xml",
    ],
    "assets": {
        "web._assets_primary_variables": [
            ("prepend", "ip_web_theme/static/src/scss/colors.scss"),
            (
                "before",
                "ip_web_theme/static/src/scss/colors.scss",
                "ip_web_theme/static/src/scss/colors_light.scss",
            ),
            (
                "after",
                "web/static/src/scss/primary_variables.scss",
                "ip_web_theme/static/src/scss/variables.scss",
            ),
            "ip_web_theme/static/src/scss/variables.scss",
        ],
        "web.assets_web_dark": [
            (
                "after",
                "ip_web_theme/static/src/scss/colors.scss",
                "ip_web_theme/static/src/scss/colors_dark.scss",
            ),
            (
                "after",
                "ip_web_theme/static/src/scss/variables.scss",
                "ip_web_theme/static/src/scss/variables.dark.scss",
            ),
        ],
        "web._assets_backend_helpers": [
            "ip_web_theme/static/src/scss/mixins.scss",
        ],
        "web.assets_backend": [
            "ip_web_theme/static/src/core/**/*.*",
            "ip_web_theme/static/src/chatter/*.scss",
            "ip_web_theme/static/src/chatter/*.xml",
            "ip_web_theme/static/src/views/**/*.scss",
            "ip_web_theme/static/src/views/**/*.js",
            "ip_web_theme/static/src/scss/dashbord.scss",
            (
                "after",
                "mail/static/src/chatter/web_portal/chatter.js",
                "ip_web_theme/static/src/chatter/chatter.js",
            ),
            (
                "after",
                "mail/static/src/chatter/web/form_compiler.js",
                "ip_web_theme/static/src/views/form/form_compiler.js",
            ),
            "ip_web_theme/static/src/views/form/form_renderer.js",
            (
                "after",
                "web/static/src/core/dialog/dialog.js",
                "/ip_web_theme/static/src/core/dialog/dialog.js",
            ),
            (
                "after",
                "web/static/src/core/dialog/dialog.scss",
                "/ip_web_theme/static/src/core/dialog/dialog.scss",
            ),
            (
                "after",
                "web/static/src/core/dialog/dialog.xml",
                "/ip_web_theme/static/src/core/dialog/dialog.xml",
            ),
            (
                "after",
                "web/static/src/views/view_dialogs/select_create_dialog.js",
                "/ip_web_theme/static/src/views/view_dialogs/select_create_dialog.js",
            ),
            (
                "after",
                "web/static/src/webclient/webclient.js",
                "ip_web_theme/static/src/webclient/webclient.js",
            ),
            (
                "after",
                "web/static/src/webclient/webclient.xml",
                "ip_web_theme/static/src/webclient/webclient.xml",
            ),
            (
                "after",
                "web/static/src/webclient/webclient.js",
                "ip_web_theme/static/src/webclient/menus/app_menu_service.js",
            ),
            (
                "after",
                "web/static/src/webclient/webclient.js",
                "ip_web_theme/static/src/webclient/appsbar/appsbar.js",
            ),
            "ip_web_theme/static/src/webclient/webclient.scss",
            "ip_web_theme/static/src/webclient/appsbar/appsbar.xml",
            "ip_web_theme/static/src/webclient/appsbar/appsbar.scss",
            "ip_web_theme/static/src/webclient/**/*.xml",
            "ip_web_theme/static/src/webclient/**/*.scss",
            "ip_web_theme/static/src/webclient/**/*.js",
            "ip_web_theme/static/src/views/**/*.scss",
        ],
    },
    "images": [
        "static/description/banner.png",
        "static/description/theme_screenshot.png",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "post_init_hook": "_setup_module",
    "uninstall_hook": "_uninstall_cleanup",
}
