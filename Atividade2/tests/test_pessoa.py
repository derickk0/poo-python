import pytest
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidadefederativa import UnidadeFederativa

@pytest.fixture
def criar_pessoa():
    pessoa1 = Pessoa(55,
                    "FF",
                    "55",
                    63465,
                    "email",
                    Sexo.MASCULINO,
                    Endereco("fodase", "532", "rua fo", "4366643", "dawd", UnidadeFederativa.BAHIA),
                    )
    return pessoa1

def test_pessoa_valido(criar_pessoa):
    assert criar_pessoa.nome == "Marta"