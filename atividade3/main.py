from models.advogado import Advogado
from models.gerente import Gerente
from models.motorista import Motorista
from models.diretor import Diretor
from models.funcionario import Funcionario
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa
from models.enums.setor import Setor
from models.enums.sexo import Sexo

import os
os.system("cls || clear")

"""""
if __name__ == "__main__":
    os.system("pytest")
"""""

advogado1 = Advogado("oab", 
                     Funcionario("nomeadv", 
                                 "cpfadv", 
                                 "rgadv", 
                                 Endereco("lograadv", 
                                          "numeroendadv", 
                                          "complementoendadv", 
                                          "cependav", 
                                          "cidadeadv", UnidadeFederativa.BAHIA),
                                 Setor.JURIDICO,
                                 Sexo.MASCULINO,
                                 10000,
                                 "55 06 12"))
print("\nADVOGADO"
      f"{advogado1}")

motorista1 = Motorista("habilitacao",
                     Funcionario("nome",
                                 "cpf",
                                 "rg",
                                 Endereco("logradouro",
                                         "numeroend",
                                         "complementoend",
                                         "cepend",
                                         "cidadeend",
                                         UnidadeFederativa.RIO_DE_JANEIRO),
                                 Setor.OPERACOES,
                                 Sexo.MASCULINO,
                                 2000,
                                 "03 02 2003"))
print("\nMOTORISTA"
      f"{motorista1}")

gerente1 = Gerente(Funcionario("nome",
                             "cpf",
                             "rg",
                             Endereco("logradouro",
                                     "numero",
                                     "complemento",
                                     "cep",
                                     "cidade",
                                     UnidadeFederativa.RIO_DE_JANEIRO,),
                             Setor.MARKETING,
                             Sexo.FEMININO,
                             5000,
                             "05 03 99"))
print("\nGERENTE"
      f"{gerente1}")

diretor1 = Diretor(Funcionario("nome",
                             "cpf",
                             "rg",
                             Endereco("logradouyro",
                                     "numeroend",
                                     "complementoend",
                                     "cep",
                                     "cidade",
                                     UnidadeFederativa.SAO_PAULO),
                             Setor.ENGENHARIA,
                             Sexo.MASCULINO,
                             12000,
                             "03 06 1998"))
print("\nDIRETOR"
      f"{diretor1}")