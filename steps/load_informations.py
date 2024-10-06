import os, sys
sys.path.insert(0, "C:\\workspaces\\Delfi\\delfia-desafio1")

import pandas as pd

class Load_Informations():

    def __init__(self, engine):
        self.file_path = os.getenv("EXCEL_PATH")
        self.engine = engine


    def run(self):
        df_clients = pd.read_excel(self.file_path, engine="openpyxl")

        df_clients = df_clients.rename(columns={
            "NOME DO CLIENTE": "NomeCliente",
            "DATA DE NASCIMENTO": "DataNascimento"
        })

        df_clients.to_sql("TB_Clientes", self.engine, if_exists="append", index=False)
        print("Dados inseridos com sucesso!")
