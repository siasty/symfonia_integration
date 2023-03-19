import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def install():
  create_custom_field("Customer", {
		"label": _("Regon"),
		"fieldname": "regon",
		"fieldtype": "Data",
		"insert_after": "tax_id"
		})
