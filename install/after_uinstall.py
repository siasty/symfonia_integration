
def uinstall():
    from frappe.custom.doctype.custom_field.custom_field import delete_custom_field
    delete_custom_field("Customer", "REGON")