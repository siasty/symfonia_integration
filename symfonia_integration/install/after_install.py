import json
import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from symfonia_integration.install.translations import translations
from symfonia_integration.install.customfields import customFileds

def install():
    
    customObj = customFileds()
    translationsObj = translations()
    
    create_custom_fields(customObj.get_custom_fields_to_add())
    customObj.change_label_name(customObj.get_fields_for_modification_label())
    
    translationsObj.add_translation_list(translationsObj.get_translation_list())

