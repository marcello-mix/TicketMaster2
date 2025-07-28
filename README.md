# Gestor de Chamados - Sistema Web

Este é um sistema web para gestão de chamados, desenvolvido com Flask e SQLite para persistência local. O sistema permite registrar, visualizar, editar e excluir chamados, com uma interface visual que facilita o acompanhamento por status.

## Funcionalidades

- **Registro de Chamados**: Formulário completo com campos para número do chamado, responsável, empresa, descrição, data de agendamento e estado.
- **Dashboard Visual**: Visualização em cards coloridos por status:
  - Verde: Chamados a vencer
  - Amarelo: Chamados vencendo hoje
  - Vermelho: Chamados atrasados
  - Azul: Chamados resolvidos/fechados
- **Gerenciamento de Chamados**: Interface para listar, editar e excluir chamados.
- **Filtros**: Possibilidade de filtrar chamados por status e buscar por texto.
- **Persistência Local**: Dados armazenados em banco SQLite local.

## Requisitos

- Python 3.6 ou superior
- Pip (gerenciador de pacotes Python)

## Instalação

1. Clone ou baixe este repositório para sua máquina local.

2. Navegue até a pasta do projeto:
   ```
   cd gestor_chamados
   ```

3. Crie um ambiente virtual Python:
   ```
   python -m venv venv
   ```

4. Ative o ambiente virtual:
   - No Windows:
     ```
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```
     source venv/bin/activate
     ```

5. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Executando o Sistema

1. Com o ambiente virtual ativado, execute:
   ```
   python -m src.main
   ```

2. Acesse o sistema no navegador:
   ```
   http://localhost:5000
   ```

## Estrutura do Projeto

```
gestor_chamados/
├── venv/                  # Ambiente virtual Python
├── src/                   # Código-fonte do sistema
│   ├── models/            # Modelos de dados
│   │   └── chamado.py     # Modelo de Chamado
│   ├── routes/            # Rotas e controladores
│   │   └── chamados.py    # Rotas para gerenciamento de chamados
│   ├── static/            # Arquivos estáticos (CSS, JS)
│   │   └── css/           # Estilos CSS
│   │       └── styles.css # Estilos do sistema
│   ├── templates/         # Templates HTML
│   │   ├── index.html     # Página inicial
│   │   ├── registro_chamado.html # Formulário de registro
│   │   ├── dashboard.html # Dashboard de chamados
│   │   └── gerenciar.html # Gerenciamento de chamados
│   ├── __init__.py        # Inicialização do Flask e SQLAlchemy
│   └── main.py            # Ponto de entrada da aplicação
└── requirements.txt       # Dependências do projeto
```

## Uso do Sistema

### Registro de Chamados

1. Acesse a página "Registrar Chamado" no menu superior.
2. Preencha todos os campos obrigatórios:
   - Responsável: pessoa encarregada pelo chamado
   - Empresa: empresa relacionada ao chamado
   - Descrição: detalhes do chamado
   - Data de Agendamento: data prevista para resolução
   - Estado: aberto ou fechado
3. Clique em "Registrar Chamado" para salvar.

### Dashboard

1. Acesse a página "Dashboard" no menu superior.
2. Visualize os chamados organizados em cards coloridos por status.
3. Use os botões de filtro para visualizar chamados específicos:
   - Todos: exibe todos os chamados
   - Vencidos: chamados em atraso
   - A Vencer: chamados dentro do prazo
   - Fechados: chamados já resolvidos
4. Clique em "Marcar como Resolvido" para fechar um chamado.

### Gerenciamento de Chamados

1. Acesse a página "Gerenciar Chamados" no menu superior.
2. Use a barra de busca para encontrar chamados específicos.
3. Use o filtro para visualizar chamados por estado.
4. Clique no ícone de edição para modificar um chamado.
5. Clique no ícone de exclusão para remover um chamado.

## Banco de Dados

O sistema utiliza SQLite como banco de dados local, armazenado no arquivo `chamados.db`. Não é necessária nenhuma configuração adicional para o banco de dados, pois ele é criado automaticamente na primeira execução do sistema.

## Personalização

Você pode personalizar o sistema editando os arquivos CSS em `src/static/css/` ou modificando os templates HTML em `src/templates/`.

## Suporte

Para dúvidas ou problemas, entre em contato com o desenvolvedor.
