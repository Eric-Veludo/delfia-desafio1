from steps.consolidate_information import Consolidate_Information
from steps.load_informations import Load_Informations
from steps.process_age import Process_Age
from steps.get_uf import Get_UF
from config import Config
from helpers.db import DB

class Main():

    def __init__(self):
        Config()
        
        db = DB()
        engine = db.get_engine()

        step_load_informations = Load_Informations(engine)
        step_process_age = Process_Age(engine)
        step_get_uf = Get_UF()
        step_consolidate_information = Consolidate_Information(engine)

        step_load_informations.run()
        lst_clients = step_process_age.run()
        step_get_uf.run(lst_clients)
        step_consolidate_information.run(lst_clients)
        

Main()
