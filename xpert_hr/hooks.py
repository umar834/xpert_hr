from . import __version__ as app_version

app_name = "xpert_hr"
app_title = "XPERT HR"
app_publisher = "MicroMerger"
app_description = "New features for stock and HR modules"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "m.gulzar@pk.micromerger.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/xpert_hr/css/xpert_hr.css"
# app_include_js = "/assets/xpert_hr/js/xpert_hr.js"

# include js, css files in header of web template
# web_include_css = "/assets/xpert_hr/css/xpert_hr.css"
# web_include_js = "/assets/xpert_hr/js/xpert_hr.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "xpert_hr/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Item" : "public/js/item.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "xpert_hr.install.before_install"
# after_install = "xpert_hr.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "xpert_hr.uninstall.before_uninstall"
# after_uninstall = "xpert_hr.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "xpert_hr.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Item": "xpert_hr.overrides.CustomItem",
	"Asset Movement": "xpert_hr.doctype_overrides.asset_movement.CustomAssetMovement",
	# "Customize Form": "xpert_hr.doctype_overrides.customize_form.CustomCustomizeForm"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"xpert_hr.tasks.all"
# 	],
# 	"daily": [
# 		"xpert_hr.tasks.daily"
# 	],
# 	"hourly": [
# 		"xpert_hr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"xpert_hr.tasks.weekly"
# 	]
# 	"monthly": [
# 		"xpert_hr.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "xpert_hr.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "xpert_hr.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "xpert_hr.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"xpert_hr.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
