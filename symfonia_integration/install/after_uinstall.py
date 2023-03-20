import frappe
from frappe import _

def uinstall():
    custom_fields = frappe.get_all("Custom Field", filters={"dt": "Customer"})
    for cf in custom_fields:
        frappe.delete_doc("Custom Field", cf.name)
    frappe.db.commit()