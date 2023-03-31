from dataclasses import dataclass


@dataclass
class HMFCustomerModel():
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
    def __post_init__(self):
        if self.Id is None:
            self.Id = '0'
       


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
