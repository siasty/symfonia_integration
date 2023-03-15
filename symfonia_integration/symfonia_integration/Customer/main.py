from __future__ import unicode_literals
import requests
import frappe
import json


def addCustomer(customer, state):
  with open('globals.json') as f:
    content = json.load(f)

  frappe.msgprint(content)