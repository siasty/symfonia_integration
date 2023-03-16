from __future__ import unicode_literals
import requests
import frappe
import json
import os


def addCustomer(customer, state):
    # api_url = "https://jsonplaceholder.typicode.com/todos"
    # todo = {
    #     "Active": true,
    #     "Code": customer.name,
    #     "Name": customer.name,
    #     "Vies": false,
    #     "VATTaxPayer": true,
    #     "SplitPayment": 0,
    #     "NIP": customer.tax_id,
    #     "Regon": "140045209",
    #     "Pesel": "",
    #     "CreditLimit": true,
    #     "MaxCreditValue": 10.0,
    #     "CreditCurrency": "PLN",
    #     "Type": 0,
    #     "Contact": {
    #         "Name": "",
    #         "Surname": "",
    #         "Phone1": "22 455 56 00",
    #         "Phone2": "",
    #         "Fax": "22 455 57 00",
    #         "Telex": "",
    #         "Email": "kontakt@sage.com.pl",
    #         "WWW": "www.sage.com.pl",
    #         "Facebook": ""
    #     },
    #     "Address": {
    #         "Country": "NL",
    #         "City": "Warszawa",
    #         "Province": "",
    #         "Street": "J. Bema",
    #         "HouseNo": "89",
    #         "ApartmentNo": "",
    #         "PostCode": "01-233"
    #     },
    #     "BankInfo": null
    # }
    frappe.msgprint(repr(customer))
