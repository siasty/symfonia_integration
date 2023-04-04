from dataclasses import dataclass
from typing import List


@dataclass
class ErpNextCustomerModel:
    name: str
    owner: str
    creation: str
    modified: str
    modified_by: str
    docstatus: int
    idx: int
    naming_series: str
    salutation: str
    customer_name: str
    customer_type: str
    customer_group: str
    territory: str
    gender: str
    default_price_list: str
    default_bank_account: str
    default_currency: str
    is_internal_customer: int
    market_segment: str
    industry: str
    website: str
    language: str
    customer_details: str
    customer_primary_contact: str
    mobile_no: str
    email_id: str
    customer_primary_address: str
    primary_address: str
    tax_id: str
    tax_category: str
    default_commission_rate: float
    so_required: int
    dn_required: int
    is_frozen: int
    disabled: int
    doctype: str
    accounts: List
    sales_team: List
    credit_limits: List
    companies: List
