import frappe
from frappe import _

def uinstall():
  #  frappe.db.delete("Customer", {"name": "regon"})
  #  frappe.db.delete("Customer", {"name": "pesel"})
  #  frappe.db.delete("Customer", {"name": "split_payment"})
    custom_fields = frappe.get_all("Custom Field", filters={"dt": "Customer"})
    for cf in custom_fields:
        print(cf.name)
    #frappe.delete_doc("Custom Field", cf.name)
    #frappe.delete_doc("Custom Field", "Customer-regon")
    #frappe.db.commit()