import json
from automapper import mapper
from dataclasses import dataclass
from typing import List


class ErpNextCustomerModel:
    def __init__(self, name:str, customer_name:str,tax_id:str):
        self.name = name
        self.customer_name = customer_name
        self.tax_id = tax_id

class HMFCustomerModel:
    def __init__(self,Code:str,Name:str,NIP:str):
        self.Code = Code
        self.Name = Name
        self.NIP = NIP


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


customer = ErpNextCustomerModel(
    name = "Cazacu Sergiu",
    customer_name = "Cazacu Sergiu",
    tax_id = "8992489312"
)




SymfoniaObj = SymfoniaContractorModel()
test = SymfoniaObj.set_maping(customer, SymfoniaModules.HMF)
jsonstr = json.dumps(vars(test))
print(jsonstr)
