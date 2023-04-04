from dataclasses import dataclass


@dataclass
class HMFCustomerModel():
    def __init__(self):
        self = {}
        
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
    PaymentRegistry: None
    PaymentForm: None
    Contact: None
    DefaultAddress: None
    CorrespondenceAddress: None
    BankInfo: None
    def __post_init__(self):
        if self.PaymentRegistry is None:
           self.PaymentRegistry = PaymentRegistry()
        if self.PaymentForm is None:
           self.PaymentForm = PaymentForm()
        if self.Contact is None:
           self.Contact = Contact()
        if self.DefaultAddress is None:
           self.DefaultAddress = DefaultAddress()
        if self.CorrespondenceAddress is None:
           self.CorrespondenceAddress = CorrespondenceAddress()
        if self.BankInfo is None:
           self.BankInfo = BankInfo()
       


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
