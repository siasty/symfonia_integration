import json
from symfonia_integration.helper.funtions import SymfoniaObjectConvert
from symfonia_integration.helper.models.ErpNextCustomerModel import ErpNextCustomerModel
from symfonia_integration.helper.models.SymphoniaCustomerModel import HMFCustomerModel
from automapper import mapper
from frappe.desk.form.meta import get_meta


class SymfoniaModules:
    HMF = 0
    FKF = 1


# SymfoniaModules = SymfoniaModules()


class SymfoniaContractorModel:
 
    def __get_symfonia_map_fields(self, type: SymfoniaModules):
        match type:
            case SymfoniaModules.HMF:
                return {
                    "Code": "Customer.name",
                    "Name": "Customer.customer_name",
                    "NIP": "Customer.tax_id",
                    "Regon": "Customer.regon",
                    "Pesel": "Customer.pesel"
                }
 
    def __get_contractor_model_by_type(self, modelType):
        match modelType:
            case SymfoniaModules.HMF:
                return HMFCustomerModel()

    def set_maping(self, customer, modyleType):

        mapper.add(ErpNextCustomerModel(),
                   self.__get_contractor_model_by_type(modyleType),
                   fields_mapping=self.__get_symfonia_map_fields(modyleType))
        return mapper.map(customer, use_deepcopy=False)
