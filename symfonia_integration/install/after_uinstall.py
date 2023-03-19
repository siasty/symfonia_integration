import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import delete_custom_field

def uinstall():
    delete_custom_field("Customer", "regon")