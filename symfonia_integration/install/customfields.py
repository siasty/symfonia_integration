

import frappe


class customFileds:
    def get_fields_for_modification_label(self):
        return [
            ("Address", "address_line1", "Street"),
            ("Address", "address_line2", "House No/Apartment No"),
        ]

    def get_fields_for_recovery_label(self):
        return [
            ("Address", "address_line1", "Address Line 1"),
            ("Address", "address_line2", "Address Line 2"),
        ]

    def get_custom_fields_to_add(self):
        return {
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
                    "label": "Symphony",
                    "fieldname": "symphony_integration",
                    "fieldtype": "Tab Break",
                    "insert_after": "disabled"
                },
                {
                    "label": "Symphony Sync",
                    "fieldname": "symphony_sync",
                    "fieldtype": "Check",
                    "insert_after": "symphony_integration",
                    "default": 0
                }
            ]
        }

    def change_label_name(self, field_list):
        for parent, fieldname, label in field_list:
            frappe.db.sql(
                "UPDATE `tabDocField` SET `label` = %s WHERE `fieldname` = %s AND `parent` = %s", (label, fieldname, parent))
        frappe.clear_cache()

    def delete_all_custom_fields_by_doctype(self,docType):
        custom_fields = frappe.get_all("Custom Field", filters={"dt": docType})
        for cf in custom_fields:
            frappe.delete_doc("Custom Field", cf.name)
        frappe.db.commit()
