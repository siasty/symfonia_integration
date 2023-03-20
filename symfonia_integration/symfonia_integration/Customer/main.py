from __future__ import unicode_literals
import requests
import frappe
import json
import os


def addCustomer(customer,state):
  frappe.msgprint(str(customer))


def convert_dict_to_class(dict_data, class_name):
  # Create an empty object of class_name using globals function
  obj = globals()[class_name]()

  for key, value in dict_data.items():
    if isinstance(value, dict):
      setattr(obj, key, convert_dict_to_class(value, key))
    elif isinstance(value, list) and all(isinstance(item, dict) for item in value):
      obj_list = []
      for item in value:
        obj_list.append(convert_dict_to_class(item, key))
      setattr(obj, key, obj_list)
    else:
      setattr(obj, key, value)
  return obj
