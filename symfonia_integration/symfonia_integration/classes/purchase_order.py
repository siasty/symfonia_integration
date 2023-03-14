from __future__ import unicode_literals
import frappe
import json
import calendar
from frappe.model.document import Document
from frappe.utils import flt

class test(Document):
  pass

  def testFunc():
    frappe.msgprint("Test")
