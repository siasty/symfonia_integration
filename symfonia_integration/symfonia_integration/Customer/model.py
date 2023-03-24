import json
from types import SimpleNamespace
from collections import namedtuple
from symfonia_integration.helper.funtions import SymfoniaObjectConvert


class SymfoniaContractorModel:
    def __HMF_Contractor_Model(self):
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

    def __FKF_Contractor_Model(self):
        return {
            "Active": True,
            "Code": "",
            "Name": "",
            "Vies": False,
            "VATTaxPayer": True,
            "SplitPayment": 0,
            "NIP": "",
            "Regon": "",
            "Pesel": "",
            "CreditLimit": True,
            "MaxCreditValue": 10.0,
            "CreditCurrency": "",
            "Type": 0,
            "Contact": {
                "Name": "",
                "Surname": "",
                "Phone1": "",
                "Phone2": "",
                "Fax": "",
                "Telex": "",
                "Email": "",
                "WWW": "",
                "Facebook": ""
            },
            "Address": {
                "Country": "",
                "City": "",
                "Province": "",
                "Street": "",
                "HouseNo": "",
                "ApartmentNo": "",
                "PostCode": ""
            },
            "BankInfo": None
        }

    def get_symfonia_hmf_contractor_model(self):
        return SymfoniaObjectConvert(self.__HMF_Contractor_Model())
    
    def get_symfonia_fkf_contractor_model(self):
        return SymfoniaObjectConvert(self.__FKF_Contractor_Model())
