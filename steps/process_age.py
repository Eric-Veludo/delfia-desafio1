import sys
sys.path.insert(0, "C:\\workspaces\\Delfi\\delfia-desafio1")

import pandas as pd
from models.client import Client

class Process_Age():
    
    def __init__(self, engine):
        self.engine = engine


    def run(self):
        query = "SELECT * FROM TB_Clientes"

        df_clients = pd.read_sql(query, self.engine)
        
        lst_clients = []
        for _, row in df_clients.iterrows():
            client = Client(row)
            lst_clients.append(client)

        return lst_clients
