import requests

class Get_UF():
    
    def run(self, lst_clients):
        for client in lst_clients:
            uf = self.get_uf(client.cep)
            client.uf = uf


    def get_uf(self, cep):
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()
            if 'erro' not in dados:
                return dados["uf"]
            else:
                return "CEP Inválido"
        else:
            print("Erro ao consultar o CEP.")        
        
        raise Exception("Erro ao consultar CEP.")
