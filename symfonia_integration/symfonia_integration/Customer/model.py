import json


class SymfoniaCustomerModel:
    def __customer_model(self):
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
            "MaxCreditValue": 0,
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
        
    def get_symfonia_customer_model(self):
        data = self.__customer_model()
        return type("Customer", (object,), data)

