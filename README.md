# Stark Bank API Integration

## Descrição

Este projeto consiste em uma aplicação desenvolvida em Python, utilizando o framework FastAPI, para integrar com a API do Stark Bank. A aplicação executa diversas rotinas, como criação de invoices, captura de webhooks com informações de pagamento e crédito de invoices, e realização de transferências financeiras entre contas a partir do aviso de crédito.

## Funcionalidades

- Criação de invoices utilizando um arquivo YAML preparado para execução através do pipeline do GitHub Actions.
- Captura de eventos de invoices, não capturados pelo endpoint configurado para o webhook, por meio de rotine diária executada através do pipeline do GitHub Actions.
- Armazenamento de todos os dados em um dataset MySQL.
- Implementação de testes unitários para garantir a integridade das funcionalidades.

## Utilização

### Pré-requisitos

- Python 3.x instalado.
- Banco de dados MySQL configurado e acessível.
- Credenciais da API do Stark Bank.
- Certificado SSL.

### Instalação

1. Clone este repositório:

   ```
   git clone https://github.com/diaslgg/StarkBankCase.git
   ```

2. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente necessárias, incluindo as credenciais da API do Stark Bank e as configurações de acesso ao banco de dados MySQL.

### Execução

Execute a aplicação com o seguinte comando.

```
uvicorn src.main:app --ssl-keyfile ../httpsKeys/key.pem --ssl-certfile ../httpsKeys/cert.pem
```

### Execução dos Testes

Para executar os testes unitários, utilize o seguinte comando:

```
pytest
```

### Configuração do GitHub Actions

Para configurar a execução automática das rotinas de criação de invoices, edite os arquivos YAML localizado em `.github/workflows`. É possível definir a frequência e o horário de execução das tarefas.

