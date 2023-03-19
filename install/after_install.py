import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def install():
    custom_fields = {
        "Customer": [
            {
                "label": "Regon",
                "fieldname": "regon",
                "fieldtype": "Data",
	            "insert_after": "tax_id"
            }
        ]
    }
    create_custom_fields(custom_fields)

