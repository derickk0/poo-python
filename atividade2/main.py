"""""
import os
from models.enums.sexo import Sexo
from models.pessoa import Pessoa
from models.endereco import Endereco
from models.enums.unidadefederativa import UnidadeFederativa

os.system("cls || clear")

pessoa1 = Pessoa(556677,
                 "nome",
                 "55 / 55 / 2055",
                 53574584,
                 "email",
                 Sexo.MASCULINO,
                 Endereco("sla qq isso",
                          "numero",
                          "rua",
                          "63646436",
                          "ja",
                          UnidadeFederativa.RIO_DE_JANEIRO
                          )
                 )

print(pessoa1)
"""""

import os
os.system("cls || clear")

if __name__ == "__main__":
    os.system("pytest")