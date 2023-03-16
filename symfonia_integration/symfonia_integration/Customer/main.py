from __future__ import unicode_literals
import requests
import frappe
import json
import os


def addCustomer(customer, state):
  frappe.msgprint(repr(customer))
