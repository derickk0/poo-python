import pytest
from atividade2.models.pessoa import Pessoa
from atividade2.models.endereco import Endereco
from atividade2.models.enums.sexo import Sexo
from atividade2.models.endereco import Endereco
from atividade2.models.enums.unidadefederativa import UnidadeFederativa

@pytest.fixture
def criar_pessoa():
    pessoa1 = Pessoa(55,
                    "nome",
                    "55",
                    63465,
                    "email",
                    Sexo.MASCULINO,
                    Endereco("logra", "numero532", "refrua", "cep4366643", "cidade", UnidadeFederativa.BAHIA),
                    )
    return pessoa1

def test_pessoa_valido(criar_pessoa):
    assert criar_pessoa.nome == "nome"

def test_pessoa_idade(criar_pessoa):
    assert criar_pessoa.id == 55