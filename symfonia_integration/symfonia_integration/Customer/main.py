from __future__ import unicode_literals
import frappe
import json
from frappe.contacts.doctype.address.address import Address
from frappe.contacts.doctype.contact.contact import Contact
from symfonia_integration.symfonia_integration.Customer.model import SymfoniaContractorModel
from frappe.desk.form.meta import get_meta
from datetime import datetime

def date_converter(o):
    if isinstance(o, datetime):
        return o.__str__()

def addCustomer(customer, state):
    SymfoniaObj = SymfoniaContractorModel()
    SymfoniaCustomerObj = SymfoniaObj.get_symfonia_hmf_contractor_model()

    meta = get_meta("Customer")
    meta_dict = meta.fields.as_dict()
    meta_json = json.dumps(meta_dict, default=date_converter)
    frappe.msgprint(meta_json)
    
    
    
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
    # jsonstr=json.dumps(vars(SymfoniaCustomerObj))
    # frappe.msgprint(jsonstr)
#    frappe.msgprint(str(customer.name))
