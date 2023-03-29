from __future__ import unicode_literals
import frappe
import json
from frappe.contacts.doctype.address.address import Address
from frappe.contacts.doctype.contact.contact import Contact
from symfonia_integration.symfonia_integration.Customer.model import SymfoniaContractorModel,SymfoniaModules
from frappe.desk.form.meta import get_meta

def addCustomer(customer, state):
    SymfoniaObj = SymfoniaContractorModel()

    # meta = get_meta("Customer")
    # meta_dict = meta.fields
    # my_list = []
    # for field in meta_dict:
    #     my_list.append(field.fieldname)
    # meta_json = json.dumps(my_list, indent=4)
    # frappe.msgprint(meta_json)
    
    
    
    # try:
    #     customer.customer_primary_address
    # except NameError:
    #     print("customer_primary_address is not set for "+ customer.name)
    # else:    
    #     if customer.customer_primary_address is not None:
    #         address = Address.get(customer.customer_primary_address)
    # try:
    #     customer.customer_primary_contact
    # except NameError:
    #     print("customer_primary_contact is not set for "+ customer.name)
    # else:  
    #     if customer.customer_primary_contact is not None:
    #         contact = Contact.get(customer.customer_primary_contact)
    test = SymfoniaObj.set_maping(customer,SymfoniaModules.HMF)
    jsonstr=json.dumps(vars(test))
    frappe.msgprint(jsonstr)
#    frappe.msgprint(str(customer.name))
