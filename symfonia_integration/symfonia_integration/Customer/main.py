from __future__ import unicode_literals
import frappe
import json
import requests
from frappe.contacts.doctype.address.address import Address
from frappe.contacts.doctype.contact.contact import Contact


def addCustomer(customer, state):
    url = "http://localhost:9000/api/Contractors/Create?syncFK=True"

    primary_address = frappe.get_doc("Customer", customer.name ).get_primary_address()
    frappe.msgprint(json.dumps(primary_address))
    # payload = json.dumps({
    #     "Active": not bool(customer.disabled),
    #     "Code": customer.name,
    #     "Name": customer.name,
    #     "Vies": False,                        # TO DO map
    #     "VATTaxPayer": False,                 # TO DO map
    #     "SplitPayment": 2,  
    #     "NIP": customer.tax_id,
    #     "PriceNegotiation": True,             # TO DO map
    #     "Type": 0,                            # TO DO map
    #     "Note": customer.customer_details,
    #     "Contact": {
    #         "Name": "",
    #         "Surname": "",
    #         "Phone1": "",
    #         "Phone2": "",
    #         "Fax": "",
    #         "Email": "kontakt@eastsoft.pl",
    #         "WWW": "eastsoft.pl",
    #         "Facebook": "www.facebook.com/eastsoftSpzoo/"
    #     },
    #     "DefaultAddress": {
    #         "Country": "PL",
    #         "City": "Siedlce",
    #         "Province": "",
    #         "Street": "Katedralna",
    #         "HouseNo": "7",
    #         "ApartmentNo": "",
    #         "PostCode": "08-110"
    #     }
    # })

    # headers = {
    #     'Authorization': 'Session {{token}}',
    #     'Content-Type': 'application/json'
    # }

    # response = requests.request("POST", url, headers=headers, data=payload)
    # frappe.msgprint(response.text)
