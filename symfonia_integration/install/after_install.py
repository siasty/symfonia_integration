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
            },
            {
                "label": "Symfonia Sync",
                "fieldname": "symfonia_sync",
                "fieldtype": "Check",
                "default": 0
            }
        ]
    }
    create_custom_fields(custom_fields)
    doc = frappe.get_doc("DocType", "Address")
    field = doc.get("fields", {"fieldname": "address_line1"})
    print(str(field))
    field.label = _("Ulica")
    # doc.save()




def change_label_name(doc):
    frappe.db.set_value('DocField', doc.name, 'label', _(doc.field_name))
