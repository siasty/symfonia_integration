import frappe
from frappe import _

def uinstall():
    _.db.delete("Customer", {"name": "regon"})
    _.db.delete("Customer", {"name": "pesel"})
    _.db.delete("Customer", {"name": "split_payment"})
    _.db.commit()