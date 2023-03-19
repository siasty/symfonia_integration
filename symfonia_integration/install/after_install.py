import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def install():
    custom_fields = {
        "Customer": [
            {
                "label": "Regon",
                "fieldname": "regon",
                "fieldtype": "Data",
	            "insert_after": "tax_id"
            },
            {
                "label": "Pesel",
                "fieldname": "pesel",
                "fieldtype": "Data",
	            "insert_after": "regon"
            },
            {
                "label": "Split Payment",
                "fieldname": "split_payment",
                "fieldtype": "Check",
		        "default": 0,
	            "insert_after": "pesel"
            }
        ]
    }
    create_custom_fields(custom_fields)

