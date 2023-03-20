import frappe
from frappe import _

def uinstall():
  #  frappe.db.delete("Customer", {"name": "regon"})
  #  frappe.db.delete("Customer", {"name": "pesel"})
  #  frappe.db.delete("Customer", {"name": "split_payment"})
    frappe.delete_doc("Custom Field", "Customer-regon")
    frappe.db.commit()