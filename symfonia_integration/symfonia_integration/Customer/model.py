import json
from symfonia_integration.helper.funtions import SymfoniaObjectConvert
from automapper import mapper
from frappe.desk.form.meta import get_meta


class SymfoniaModules:
    HMF = 0
    FKF = 1

SymfoniaModules = SymfoniaModules()

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

    def __get_symfonia_map_fields(self, type: SymfoniaModules):
        match type:
            case SymfoniaModules.FKF:
                return {
                    "Code": "Customer.name",
                    "Name": "Customer.customer_name",
                    "NIP": "Customer.tax_id",
                    #   "Regon":"Customer.regon",
                    #   "Pesel":"Customer.pesel"
                }
            case SymfoniaModules.HMF:
                return {
                    "Code": "Customer.name",
                    "Name": "Customer.customer_name",
                    "NIP": "Customer.tax_id",
                    "Regon": "Customer.regon",
                    "Pesel": "Customer.pesel"
                }

    def __get_symfonia_hmf_contractor_model(self):
        return SymfoniaObjectConvert(self.__HMF_Contractor_Model())

    def __get_symfonia_fkf_contractor_model(self):
        return SymfoniaObjectConvert(self.__FKF_Contractor_Model())

    def __get_contractor_model_by_type(self, modelType):
        match modelType:
            case SymfoniaModules.FKF:
                return self.__get_symfonia_fkf_contractor_model()
            case SymfoniaModules.HMF: 
                return self.__get_symfonia_hmf_contractor_model()

    def set_maping(self, customer, modyleType):
        mapper.add(SymfoniaObjectConvert(customer),
                   self.__get_contractor_model_by_type(modyleType),
                   fields_mapping = self.__get_symfonia_map_fields(modyleType))
        return mapper.map(customer, use_deepcopy = False)
