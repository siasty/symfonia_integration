from __future__ import unicode_literals
import frappe
import json
import calendar
from frappe.model.document import Document
from frappe.utils import flt

def testFunc(doc, state):
  frappe.msgprint("Test - par doc:"+doc+" state:"+state)
