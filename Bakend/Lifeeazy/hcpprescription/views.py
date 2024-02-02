from .hcpprescription_crud.get_hcp_lab_records_api import GetHcpLabRecordsAPI
from .hcpprescription_crud.get_hcp_prescription_api import Data
from .hcpprescription_crud.hcp_lab_records import HcpLabRecords
from .hcpprescription_crud.hcp_lab_records_byId import HcpLabRecordsById
from .hcpprescription_crud.hcp_presciption_byId import HcpPresciptionById
from .hcpprescription_crud.hcp_prescription_reg_api import HcpPrescriptionRegAPI
from .hcpprescription_crud.get_prescription_by_userid import HcpPresciptionByUserId


GetHcpLabRecordsAPI()  # This is a get for getting the lab records
Data () # This is a get for getting the medical prescription details
HcpLabRecords()  # This is a post of the lab records
HcpLabRecordsById()  # This is a get for getting lab records by doctor id
HcpPresciptionById()  # This is a get for getting medical prescription records by doctor id
HcpPrescriptionRegAPI()  # This is a post of the medical prescription records
HcpPresciptionByUserId()
