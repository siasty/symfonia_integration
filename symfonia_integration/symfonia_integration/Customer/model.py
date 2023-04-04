import json
from symfonia_integration.helper.models.ErpNext.ErpNextCustomerModel import ErpNextCustomerModel
from symfonia_integration.helper.models.Symphony.SymphonyCustomerModel import HMFCustomerModel
from automapper import mapper
from frappe.desk.form.meta import get_meta


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
                    "NIP": "ErpNextCustomerModel.tax_id",
                    "Regon": "ErpNextCustomerModel.regon",
                    "Pesel": "ErpNextCustomerModel.pesel"
                }
 
    def __get_contractor_model_by_type(self, modelType):
        match modelType:
            case SymfoniaModules.HMF:
                return HMFCustomerModel

    def set_maping(self, customer, modyleType):
        cust = mapper.to(ErpNextCustomerModel).map(customer)

        mapper.add(ErpNextCustomerModel,
                   self.__get_contractor_model_by_type(modyleType),
                   fields_mapping=self.__get_symfonia_map_fields(modyleType))
        return mapper.map(cust, use_deepcopy=False)
