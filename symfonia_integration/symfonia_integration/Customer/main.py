from __future__ import unicode_literals
import requests
import frappe
import json
import os


def addCustomer(customer, state):
  # Get the current working directory
  cwd = os.getcwd()

#  with open('globals.json') as f:
#    content = json.load(f)

  frappe.msgprint(cwd)