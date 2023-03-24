from __future__ import unicode_literals
import frappe
import json
from frappe.contacts.doctype.address.address import Address
from frappe.contacts.doctype.contact.contact import Contact
from symfonia_integration.symfonia_integration.Customer.model import SymfoniaCustomerModel


def addCustomer(customer, state):
    SymfoniaObj = SymfoniaCustomerModel()
    SymfoniaCustomerObj = SymfoniaObj.get_symfonia_customer_model()
    #map
    SymfoniaCustomerObj.Name = customer.customer_name
    SymfoniaCustomerObj.Code = customer.name
    SymfoniaCustomerObj.NIP = customer.tax_id
    SymfoniaCustomerObj.Regon = customer.regon
    SymfoniaCustomerObj.Pesel = customer.pesel
    
    try:
        customer.customer_primary_address
    except NameError:
        print("customer_primary_address is not set for "+ customer.name)
    else:    
        if customer.customer_primary_address is not None:
            address = Address.get(customer.customer_primary_address)
    try:
        customer.customer_primary_contact
    except NameError:
        print("customer_primary_contact is not set for "+ customer.name)
    else:  
        if customer.customer_primary_contact is not None:
            contact = Contact.get(customer.customer_primary_contact)
    
    frappe.msgprint(str(SymfoniaCustomerObj.Name))
#    frappe.msgprint(str(customer.name))
