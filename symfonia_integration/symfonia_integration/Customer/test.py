import json
from automapper import mapper
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ErpNextCustomerModel:
    name:str
    customer_name:str
    tax_id:str
    # def __init__(self, name:str, customer_name:str,tax_id:str):
    #     self.name = name
    #     self.customer_name = customer_name
    #     self.tax_id = tax_id

@dataclass
class HMFCustomerModel:
    Id: int = field(init=False)
    Active: bool = field(init=False)
    Code: str 
    Name: str
    Vies: bool = field(init=False) 
    VATTaxPayer: bool  = field(init=False)
    NIP: str = field(init=False)
    Pesel: str = field(init=False)
    CreditLimit: bool = field(init=False)
    MaxCreditValue: int = field(init=False)
    CreditCurrency: str = field(init=False)
    PriceNegotiation: bool = field(init=False)
    DefaultDiscountPercent: int = field(init=False)
    PriceType: int = field(init=False) 
    PriceKind: int = field(init=False)
    Type: int = field(init=False)
    Note: str = field(init=False)
    Marker: int = field(init=False)
    Due: int = field(init=False)
    Obligation: int = field(init=False)
    PaymentRegistry: PaymentRegistry = field(init=False)
    PaymentForm: PaymentForm = field(init=False) 
    Contact: Contact = field(init=False)
    DefaultAddress: DefaultAddress = field(init=False)
    CorrespondenceAddress: CorrespondenceAddress = field(init=False) 
    BankInfo: BankInfo = field(init=False)       


@dataclass
class PaymentRegistry:
    Id: int
    Code: str
    def __post_init__(self):
        if self.Id is None:
            self.Id = '0'
            self.Code = ''


@dataclass
class PaymentForm:
    Id: int
    Client: int
    def __post_init__(self):
        if self.Id is None:
            self.Id = '0'

@dataclass
class Contact:
    Name: str
    Surname: str
    Phone1: str
    Phone2: str
    Fax: str
    Email: str
    WWW: str
    Facebook: str


@dataclass
class DefaultAddress:
    Type: int
    Country: str
    City: str
    Province: str
    Street: str
    HouseNo: str
    ApartmentNo: str
    PostCode: str
    def __post_init__(self):
        if self.Type is None:
            self.Type = '1'


@dataclass
class CorrespondenceAddress:
    Type: int
    Country: str
    City: str
    Province: str
    Street: str
    HouseNo: str
    ApartmentNo: str
    PostCode: str
    def __post_init__(self):
        if self.Type is None:
            self.Type = '2'

@dataclass
class BankInfo:
    AccountNumber: str
    BankName: str
    SWIFT_BIC: str

class SymfoniaModules:
    HMF = 0
    FKF = 1


class SymfoniaContractorModel:

    def __get_symfonia_map_fields(self, type: SymfoniaModules):
        match type:
            case SymfoniaModules.HMF:
                return {
                    "Code": "ErpNextCustomerModel.name",
                    "Name": "ErpNextCustomerModel.customer_name",
                    "NIP": "ErpNextCustomerModel.tax_id"
                }

    def __get_contractor_model_by_type(self, modelType):
        match modelType:
            case SymfoniaModules.HMF:
                return HMFCustomerModel

    def set_maping(self, customer, modyleType):

        mapper.add(ErpNextCustomerModel,
                   self.__get_contractor_model_by_type(modyleType),
                   fields_mapping=self.__get_symfonia_map_fields(modyleType))
        return mapper.map(customer, use_deepcopy=False)



customer = {
      "name": "Cazacu Sergiu",
      "customer_name": "Cazacu Sergiu",
      "tax_id": "8992489312"
}
cust = mapper.to(ErpNextCustomerModel).map(customer)



SymfoniaObj = SymfoniaContractorModel()
test = SymfoniaObj.set_maping(cust, SymfoniaModules.HMF)
jsonstr = json.dumps(vars(test))
print(jsonstr)
