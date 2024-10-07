from operator import attrgetter
from itertools import groupby
import pandas as pd

class Consolidate_Information():

    def __init__(self, engine):
        self.engine = engine

    
    def  run(self, lst_clients):
        # Agrupando pelo atributo 'UF'
        lst_clients.sort(key=attrgetter('uf'))
        clients_grouped_by_uf = groupby(lst_clients, key=attrgetter('uf'))

        for uf, group in clients_grouped_by_uf:
            uf_age_group = self.group_by_age(uf, group)
            df_uf_age_group = pd.DataFrame([uf_age_group])
            df_uf_age_group.to_sql("TB_Faixa_Etaria", self.engine, if_exists="append", index=False)


    def group_by_age(self, uf, group):
        twenty_to_thirty = 0
        thirty_one_to_sixty = 0
        more_than_sixty = 0

        for client in group:
            if(client.idade >= 20 and client.idade <= 30):
                twenty_to_thirty += 1
            elif(client.idade > 30 and client.idade <=60):
                thirty_one_to_sixty += 1
            elif(client.idade > 60):
                more_than_sixty += 1

        return {
            "uf": uf,
            "twenty_to_thirty": twenty_to_thirty,
            "thirty_one_to_sixty": thirty_one_to_sixty,
            "more_than_sixty": more_than_sixty   
        }
