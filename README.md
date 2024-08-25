# APIBankingSystem

Este é um sistema de API bancária criado com FastAPI. Ele permite a criação e gerenciamento de clientes, contas bancárias e transações.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte maneira:

-> banking_app/ │ ├── app/ │ ├── init.py │ ├── main.py │ ├── api/ │ │ ├── init.py │ │ ├── endpoints/ │ │ │ ├── init.py │ │ │ ├── cliente.py │ │ │ ├── conta.py │ │ │ ├── transacao.py │ │ │ └── extrato.py │ │ └── models/ │ │ ├── init.py │ │ ├── cliente.py │ │ ├── conta.py │ │ └── transacao.py │ ├── core/ │ │ ├── init.py │ │ └── banco.py │ ├── services/ │ │ ├── init.py │ │ └── banco_service.py │ └── schemas/ │ ├── init.py │ ├── cliente.py │ ├── conta.py │ └── transacao.py │ └── tests/ ├── init.py ├── test_cliente.py ├── test_conta.py └── test_transacao.py


## Pré-requisitos

Certifique-se de que você tem o Python e o `pip` instalados. Você pode usar um ambiente virtual para gerenciar as dependências.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/MariaGabrielaAlvesZuppardo/APIBankingSystem.git
   cd seu_repositorio

2. **Crie e ative um ambiente virtual:**
python -m venv .venv
source .venv/bin/activate  # No Windows, use .venv\Scripts\activate

3. **Instale as dependências:** 
pip install fastapi uvicorn

## Uso: 

1. **Inicie o servidor :** 
uvicorn app.main:app --reload

Isso iniciará a aplicação no modo de desenvolvimento, com recarga automática ao fazer alterações.

2. **Acesse a documentação Swagger UI:**

Abra o navegador e vá para:

http://127.0.0.1:8000/docs

Esta interface permite explorar e testar os endpoints da API.

## Endpoints da API : 

Aqui estão alguns dos endpoints disponíveis:
Criar Cliente

    Método: POST
    Endpoint: /clientes/
    Corpo da Requisição: JSON

{
  "nome": "Nome do Cliente",
  "data_nascimento": "dd/mm/yyyy",
  "cpf": "12345678901",
  "endereco": "Rua X, 123 - Bairro - Cidade UF"
}


## Testes

Os testes estão localizados na pasta tests/. Você pode usar pytest para executar os testes:

pip install pytest
pytest

## Contribuições

Contribuições são bem-vindas! Por favor, envie um pull request ou abra uma issue para discutir melhorias.
Licença

Este projeto é licenciado sob a MIT License.