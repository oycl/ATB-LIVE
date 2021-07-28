# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ColorSettings(models.TransientModel):
    _inherit = "res.config.settings"

    BASE_CSS = """.o_main_navbar {
      background-color: {{ $primary-color }};
      border-bottom: 0px;
    }

    .o_main_navbar .show .dropdown-toggle {
      background-color: {{ $primary-color }};
    }

    .o_main_navbar > ul > li > a:hover,
    .o_main_navbar > ul > li > label:hover {
      background-color: {{ $secondary-color }};
    }

    .o_main_navbar > a:hover,
    .o_main_navbar > a:focus,
    .o_main_navbar > button:hover,
    .o_main_navbar > button:focus {
      background-color: {{ $secondary-color }};
      color: inherit;
    }

    .o_main_navbar > a:hover,
    .o_main_navbar > a:focus,
    .o_main_navbar > button:hover,
    .o_main_navbar > button:focus {
      background-color: {{ $secondary-color }};
      color: inherit;
    }

    .btn-primary {
      color: #ffffff !important;
      background-color: {{ $accent-color }} !important;
      border-color: {{ $accent-color }} !important;
    }

    .btn-secondary {
      background-color: white !important;
      border-color: white !important;
      color: {{ $accent-color }} !important;
    }

    .o_kanban_view.o_kanban_grouped .o_kanban_record,
    .o_kanban_view.o_kanban_grouped .o_kanban_quick_create {
      margin-top: 3px !important;
      margin-bottom: 3px !important;
      border: none !important;
    }

    .o_kanban_view.o_kanban_grouped.o_kanban_small_column
      .o_kanban_group:not(.o_column_folded) {
      background-color: #ebecf0 !important;
    }

    .btn-link {
      color: {{ $accent-color }} !important;
      text-decoration: none;
    }

    .o_searchview .o_searchview_facet .o_searchview_facet_label {
      background-color: {{ $primary-color }} !important;
    }

    .o_mail_systray_item .o_notification_counter {
      margin-top: -0.8rem;
      margin-right: 0;
      margin-left: -0.6rem;
      background: {{ $accent-color }} !important;
      color: white !important;
      vertical-align: super;
      font-size: 0.7em;
    }

    .badge {
      border: 1px solid {{ $accent-color }} !important;
    }

    .badge-pill {
      border-color: white !important;
    }

    .badge-success {
      border-color: #00a04a !important;
    }

    .o_controller_with_searchpanel
      .o_search_panel
      .o_search_panel_category
      .o_search_panel_section_icon {
      color: {{ $primary-color }} !important;
    }

    a {
      color: {{ $accent-color }} !important;
      text-decoration: none;
      background-color: transparent;
    }

    .o_web_client .o_view_grid > tfoot,
    .o_web_client .o_view_grid .o_grid_total {
      color: white !important;
      background-color: {{ $primary-color }} !important;
      text-align: right;
    }

    .custom-control-input:checked ~ .custom-control-label::before {
      color: #e9ecef;
      border-color: {{ $accent-color }} !important;
      background-color: {{ $accent-color }} !important;
    }

    .o_main_navbar > ul > li > a,
    .o_main_navbar > ul > li > label {
      color: white !important;
    }

    .o_main_navbar > .o_menu_brand {
      color: white !important;
    }

    .o_main_navbar > a,
    .o_main_navbar > button {
      color: white !important;
    }

    .dropdown-item {
      color: #666666 !important;
    }

    .o_timesheet_plan_sale_timesheet
      .o_timesheet_plan_sale_timesheet_people_time
      > .o_timesheet_plan_badge
      > .badge
      a {
      color: white !important;
    }

    .o_timesheet_plan_sale_timesheet
      .o_timesheet_plan_sale_timesheet_people_time
      > .o_timesheet_plan_badge
      > .badge {
      border: none !important;
    }

    .o_form_view .oe_button_box .btn.oe_stat_button > .o_stat_info .o_stat_value,
    .o_form_view
      .oe_button_box
      .o_account_reports_page
      .oe_stat_button.oe_link_reports
      > .o_stat_info
      .o_stat_value,
    .o_account_reports_page
      .o_form_view
      .oe_button_box
      .oe_stat_button.oe_link_reports
      > .o_stat_info
      .o_stat_value,
    .o_form_view
      .oe_button_box
      .o_radio_hide_bullet
      label.oe_stat_button
      > .o_stat_info
      .o_stat_value,
    .o_radio_hide_bullet
      .o_form_view
      .oe_button_box
      label.oe_stat_button
      > .o_stat_info
      .o_stat_value,
    .o_form_view .oe_button_box .btn.oe_stat_button > span .o_stat_value,
    .o_form_view
      .oe_button_box
      .o_account_reports_page
      .oe_stat_button.oe_link_reports
      > span
      .o_stat_value,
    .o_account_reports_page
      .o_form_view
      .oe_button_box
      .oe_stat_button.oe_link_reports
      > span
      .o_stat_value,
    .o_form_view
      .oe_button_box
      .o_radio_hide_bullet
      label.oe_stat_button
      > span
      .o_stat_value,
    .o_radio_hide_bullet
      .o_form_view
      .oe_button_box
      label.oe_stat_button
      > span
      .o_stat_value {
      color: {{ $primary-color }} !important;
    }

    .o_form_view
      .o_form_statusbar
      > .o_statusbar_status
      > .o_arrow_button.btn-primary.disabled:after {
      border-left-color: {{ $accent-color }} !important;
    }
    .o_form_view
      .o_form_statusbar
      > .o_statusbar_status
      > .o_arrow_button:not(:first-child):before {
      border-left-color: {{ $accent-color }} !important;
    }
    .o_home_menu_background {
      background-image: {{ $logo-background-url }}
        url(/web_enterprise/static/src/img/home-menu-bg-overlay.svg),
        linear-gradient(to right bottom, {{ $primary-background-color }}, {{ $secondary-background-color }}) !important;
      background-position: center center, top center;
      background-repeat: no-repeat, repeat;
      background-size: auto;
    }

    .o_form_view .oe_button_box .btn.oe_stat_button > .o_stat_info .o_stat_value,
    .o_form_view
      .oe_button_box
      .o_account_reports_page
      .oe_stat_button.oe_link_reports
      > .o_stat_info
      .o_stat_value,
    .o_account_reports_page
      .o_form_view
      .oe_button_box
      .oe_stat_button.oe_link_reports
      > .o_stat_info
      .o_stat_value,
    .o_form_view
      .oe_button_box
      .o_radio_hide_bullet
      label.oe_stat_button
      > .o_stat_info
      .o_stat_value,
    .o_radio_hide_bullet
      .o_form_view
      .oe_button_box
      label.oe_stat_button
      > .o_stat_info
      .o_stat_value,
    .o_form_view .oe_button_box .btn.oe_stat_button > span .o_stat_value,
    .o_form_view
      .oe_button_box
      .o_account_reports_page
      .oe_stat_button.oe_link_reports
      > span
      .o_stat_value,
    .o_account_reports_page
      .o_form_view
      .oe_button_box
      .oe_stat_button.oe_link_reports
      > span
      .o_stat_value,
    .o_form_view
      .oe_button_box
      .o_radio_hide_bullet
      label.oe_stat_button
      > span
      .o_stat_value,
    .o_radio_hide_bullet
      .o_form_view
      .oe_button_box
      label.oe_stat_button
      > span
      .o_stat_value {
      color: {{ $primary-color }} !important;
    }"""

    primary_color = fields.Char(
        string="Primary Color",
        help="Odoo's primary color (usually the color used in the navbar and main components)",
        default="#875a7b",
    )
    # Default secondary color in Odoo Enterprise #6e4162
    secondary_color = fields.Char(
        string="Secondary Color",
        help="Odoo's secondary color (the color for the effects of the primary color)",
        default=False,
    )
    accent_color = fields.Char(
        string="Accent Color",
        help="Odoo components accent color (usually the color for buttons and other small accents on the views)",
        default="#0c9f9c",
    )
    primary_background_color = fields.Char(
        string="Primary Background Color",
        help="Odoo's background primary color (color gradient that shows in the home page for the enterprise version)",
        default="#333333",
    )
    secondary_background_color = fields.Char(
        string="Secondary Background Color",
        help="Odoo's background secondary color (color gradient that shows in the"
        " home page for the enterprise version)",
        default="#333333",
    )
    custom_secondary = fields.Boolean(
        string="Custom Secondary Color?",
        help="Use custom secondary color or let Odoo calculate the secondary updater.",
        default=False,
    )
    logo_background_url = fields.Char(
        string="Custom Background Logo",
        help="URL for Odoo's background logo (works better with images 500x500 pixels)",
        default=False,
    )

    @api.model
    def set_values(self):
        super(ColorSettings, self).set_values()
        self.env["ir.config_parameter"].sudo().set_param(
            "updater.primary_color", self.primary_color
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "updater.secondary_color", self.secondary_color
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "updater.accent_color", self.accent_color
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "updater.primary_background_color", self.primary_background_color
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "updater.secondary_background_color", self.secondary_background_color
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "updater.custom_secondary", str(self.custom_secondary)
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "updater.logo_background_url", self.logo_background_url
        )
        self._set_colors(
            primary_color=self.primary_color,
            secondary_color=self.secondary_color,
            accent_color=self.accent_color,
            primary_background_color=self.primary_background_color,
            secondary_background_color=self.secondary_background_color,
            custom_secondary=self.custom_secondary,
            logo_background_url=self.logo_background_url,
        )

    @api.model
    def get_values(self):
        res = super(ColorSettings, self).get_values()
        primary_color = (
            self.env["ir.config_parameter"].sudo().get_param("updater.primary_color")
        )
        secondary_color = (
            self.env["ir.config_parameter"].sudo().get_param("updater.secondary_color")
        )
        accent_color = (
            self.env["ir.config_parameter"].sudo().get_param("updater.accent_color")
        )
        primary_background_color = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("updater.primary_background_color")
        )
        secondary_background_color = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("updater.secondary_background_color")
        )
        custom_secondary = (
            self.env["ir.config_parameter"].sudo().get_param("updater.custom_secondary")
            == "True"
        )
        logo_background_url = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("updater.logo_background_url")
        )
        res.update(
            primary_color=primary_color,
            secondary_color=secondary_color,
            accent_color=accent_color,
            primary_background_color=primary_background_color,
            secondary_background_color=secondary_background_color,
            custom_secondary=custom_secondary,
            logo_background_url=logo_background_url,
        )
        return res

    def _set_colors(
        self,
        primary_color: str,
        secondary_color: str,
        accent_color: str,
        primary_background_color: str,
        secondary_background_color: str,
        custom_secondary: bool,
        logo_background_url: str,
    ):
        if not custom_secondary and primary_color:
            secondary_color = self.color_variant(hex_color=primary_color)
        colors = {
            "$primary-color": primary_color,
            "$secondary-color": secondary_color,
            "$accent-color": accent_color,
            "$primary-background-color": primary_background_color,
            "$secondary-background-color": secondary_background_color,
            "$logo-background-url": logo_background_url,
        }
        colors
        # out = sass.compile(string=chevron.render(self.BASE_CSS, colors))
        # TODO: update a qweb template with the css
        # print(os.path.relpath('../..', os.path.dirname(__file__))

    @staticmethod
    def color_variant(hex_color, brightness_offset=-25):
        """ takes a color like #87c95f and produces a lighter or darker variant """
        rgb_hex = [hex_color[x : x + 2] for x in [1, 3, 5]]
        new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
        new_rgb_int = [
            min([255, max([0, i])]) for i in new_rgb_int
        ]  # make sure new values are between 0 and 255
        # hex() produces "0x88", we want just "88"
        return "#" + "".join([("0" + hex(i).split("x")[1])[-2:] for i in new_rgb_int])
