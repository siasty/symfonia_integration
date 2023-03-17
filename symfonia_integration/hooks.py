from . import __version__ as app_version

app_name = "symfonia_integration"
app_title = "Symfonia Integration"
app_publisher = "ErpTech"
app_description = "integration with the symphony system"
app_email = "maciej.miskiewicz@erptech.pl"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/symfonia_integration/css/symfonia_integration.css"
# app_include_js = "/assets/symfonia_integration/js/symfonia_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/symfonia_integration/css/symfonia_integration.css"
# web_include_js = "/assets/symfonia_integration/js/symfonia_integration.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "symfonia_integration/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "symfonia_integration.utils.jinja_methods",
#	"filters": "symfonia_integration.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "symfonia_integration.install.before_install"
after_install = "symfonia_integration.install.after_install.install"

# Uninstallation
# ------------

# before_uninstall = "symfonia_integration.uninstall.before_uninstall"
after_uninstall = "symfonia_integration.install.after_uninstall.uinstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "symfonia_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

doc_events = {
	"Customer": {
		"after_insert": "symfonia_integration.symfonia_integration.Customer.main.addCustomer",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"symfonia_integration.tasks.all"
#	],
#	"daily": [
#		"symfonia_integration.tasks.daily"
#	],
#	"hourly": [
#		"symfonia_integration.tasks.hourly"
#	],
#	"weekly": [
#		"symfonia_integration.tasks.weekly"
#	],
#	"monthly": [
#		"symfonia_integration.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "symfonia_integration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "symfonia_integration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "symfonia_integration.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["symfonia_integration.utils.before_request"]
# after_request = ["symfonia_integration.utils.after_request"]

# Job Events
# ----------
# before_job = ["symfonia_integration.utils.before_job"]
# after_job = ["symfonia_integration.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"symfonia_integration.auth.validate"
# ]
