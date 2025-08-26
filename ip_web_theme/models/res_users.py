from odoo import models, fields, api


class ResUsers(models.Model):

    _inherit = "res.users"

    # ----------------------------------------------------------
    # Properties
    # ----------------------------------------------------------

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + [
            "sidebar_type",
            "chatter_position",
            "dialog_size",
            "theme_mode",
        ]

    @property
    def SELF_WRITEABLE_FIELDS(self):
        return super().SELF_WRITEABLE_FIELDS + [
            "sidebar_type",
            "chatter_position",
            "dialog_size",
            "theme_mode",
        ]

    # ----------------------------------------------------------
    # Fields
    # ----------------------------------------------------------

    sidebar_type = fields.Selection(
        selection=[("invisible", "Invisible"), ("small", "Small"), ("large", "Large")],
        string="Sidebar Type",
        default="large",
        required=True,
    )

    chatter_position = fields.Selection(
        selection=[
            ("side", "Side"),
            ("bottom", "Bottom"),
        ],
        string="Chatter Position",
        default="side",
        required=True,
    )

    dialog_size = fields.Selection(
        selection=[
            ("minimize", "Minimize"),
            ("maximize", "Maximize"),
        ],
        string="Dialog Size",
        default="minimize",
        required=True,
    )
    theme_mode = fields.Selection(
        selection=[
            ("light", "Light"),
            ("dark", "Dark"),
        ],
        string="Theme Mode",
        default="light",
        required=True,
    )
