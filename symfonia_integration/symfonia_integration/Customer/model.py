import json
from collections import namedtuple


class SymfoniaCustomerModel:
    def __customer_model(self):
        return {
            "Id": 0,
            "Active": True,
            "Code": "",
            "Name": "",
            "Vies": True,
            "VATTaxPayer": False,
            "NIP": "",
            "Pesel": "",
            "CreditLimit": False,
            "MaxCreditValue": 0,
            "CreditCurrency": "",
            "PriceNegotiation": True,
            "DefaultDiscountPercent": 0,
            "PriceType": 1,
            "PriceKind": 1,
            "Type": 2,
            "Note": "",
            "Marker": 0,
            "Due": 0,
            "Obligation": 0,
            "PaymentRegistry": {
                "Id": 0,
                "Code": ""
            },
            "PaymentForm": {
                "Id": 0,
                "Client": 0
            },
            "Contact": {
                "Name": "",
                "Surname": "",
                "Phone1": "",
                "Phone2": "",
                "Fax": "",
                "Email": "",
                "WWW": "",
                "Facebook": ""
            },
            "DefaultAddress": {
                "Type": 1,
                "Country": "",
                "City": "",
                "Province": "",
                "Street": "",
                "HouseNo": "",
                "ApartmentNo": "",
                "PostCode": ""
            },
            "CorrespondenceAddress": {
                "Type": 2,
                "Country": "",
                "City": "",
                "Province": "",
                "Street": "",
                "HouseNo": "",
                "ApartmentNo": "",
                "PostCode": ""
            },
            "BankInfo": {
                "AccountNumber": "",
                "BankName": "",
                "SWIFT_BIC": ""
            }
        }
    
    def __SymfoniaModelDecoder(symfoniaDict):
        return namedtuple('X', symfoniaDict.keys())(*symfoniaDict.values())


    def get_symfonia_customer_model(self):
        data = self.__customer_model()
        jsonToPy=json.dumps(data)
        return json.loads(jsonToPy, object_hook=self.__SymfoniaModelDecoder)
   #     return type("Customer", (object,), data)


