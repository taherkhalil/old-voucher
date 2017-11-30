# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "voucher"
app_title = "Voucher"
app_publisher = "taher"
app_description = "voucher app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "taherkhalil52@gmail.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/voucher/css/voucher.css"
# app_include_js = "/assets/voucher/js/voucher.js"

# include js, css files in header of web template
# web_include_css = "/assets/voucher/css/voucher.css"
# web_include_js = "/assets/voucher/js/voucher.js"

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

# before_install = "voucher.install.before_install"
# after_install = "voucher.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "voucher.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
	"Sales Invoice" : {
		"validate": "voucher.voucher.doctype.voucher.voucher.on_voucher_apply"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"voucher.tasks.all"
# 	],
# 	"daily": [
# 		"voucher.tasks.daily"
# 	],
# 	"hourly": [
# 		"voucher.tasks.hourly"
# 	],
# 	"weekly": [
# 		"voucher.tasks.weekly"
# 	]
# 	"monthly": [
# 		"voucher.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "voucher.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "voucher.event.get_events"
# }

