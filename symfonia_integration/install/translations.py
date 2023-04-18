

import frappe


class translations:
    def add_translation_list(self, translations_list):

        for items in translations_list:
            translation = frappe.new_doc("Translation")
            translation.update(items)
            translation.insert()
            
    def delete_translation_list(self, translations_list):
        for items in translations_list:
            translation = frappe.get_doc("Translation",items)
            frappe.db.delete("Translation", translation.name)
        frappe.clear_cache()
            
    def get_translation_list(self):
        return [
            {
                "source_text": "Street",
                "language": "pl",
                "translated_text": "Ulica"
            },
            {
                "source_text": "House No/Apartment No",
                "language": "pl",
                "translated_text": "Nr domu/mieszkania"
            },
            {
                "source_text": "Symphony",
                "language": "pl",
                "translated_text": "Symfonia"
            },
            {
                "source_text": "Symphony Sync",
                "language": "pl",
                "translated_text": "Symfonia Sync"
            }
        ]
