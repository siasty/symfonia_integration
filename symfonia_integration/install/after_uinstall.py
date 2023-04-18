import frappe
from frappe import _
from symfonia_integration.install.customfields import customFileds
from symfonia_integration.install.translations import translations

def uinstall():

    #
    translationsObj = translations()
    customObj = customFileds()
    
    # recovery standard label
    customObj.change_label_name(customObj.get_fields_for_recovery_label())

    # delete translations
    translationsObj.delete_translation_list(translationsObj.get_translation_list())

    # deleting custom fileds
    customObj.delete_all_custom_fields_by_doctype("Customer")


    
    
    