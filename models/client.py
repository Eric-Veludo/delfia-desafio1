class Client:
    
    def __init__(self, df_row):
        self.id = df_row["id"]
        self.nome_cliente = (df_row["NomeCliente"]).strip()
        self.cep = df_row["CEP"]
        self.data_nascimento = df_row["DataNascimento"]
        self.idade = self.calcular_idade()
        self.uf = None
        

    def __repr__(self):
        return (f"Cliente(id={self.id}, nome_cliente='{self.nome_cliente}', "
                f"cep='{self.cep}', data_nascimento='{self.data_nascimento}', idade='{self.idade}', uf='{self.uf}')")


    def calcular_idade(self):
        """Calcula a idade do cliente com base na data de nascimento."""
        from datetime import date
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year
        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade -= 1
        return idade
