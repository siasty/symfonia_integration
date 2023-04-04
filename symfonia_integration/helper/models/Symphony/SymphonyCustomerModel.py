from dataclasses import dataclass, field

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
