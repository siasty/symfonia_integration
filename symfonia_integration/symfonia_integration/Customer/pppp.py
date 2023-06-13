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
    Id: int 
    Active: bool
    Code: str 
    Name: str
    Vies: bool 
    VATTaxPayer: bool 
    NIP: str 
    Pesel: str 
    CreditLimit: bool 
    MaxCreditValue: int 
    CreditCurrency: str 
    PriceNegotiation: bool 
    DefaultDiscountPercent: int 
    PriceType: int  
    PriceKind: int 
    Type: int 
    Note: str 
    Marker: int 
    Due: int 
    Obligation: int 
    PaymentRegistry: PaymentRegistry 
    PaymentForm: PaymentForm  
    Contact: Contact 
    DefaultAddress: DefaultAddress 
    CorrespondenceAddress: CorrespondenceAddress 
    BankInfo: BankInfo   
    def __init__(self, name: str, Id: int = 0):
        self.name = name
        self.Id = Id

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
