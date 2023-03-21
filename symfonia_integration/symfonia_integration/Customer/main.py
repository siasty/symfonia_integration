from __future__ import unicode_literals
import requests
import frappe
from Customer.model import *


def addCustomer(customer, state):
    SymfoniaObj = SymfoniaCustomerModel()
    SymfoniaCustomerObj = SymfoniaObj.get_symfonia_customer_model()
    SymfoniaCustomerObj.Name = customer.name
    frappe.msgprint(str(customer.name))
