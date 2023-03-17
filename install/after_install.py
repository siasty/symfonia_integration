from __future__ import unicode_literals

def install():
  from frappe.custom.doctype.custom_field.custom_field import create_custom_field
  create_custom_field("Customer", {
    "label": "REGON",
    "fieldtype": "Text",
    "lenght":"9"
  })