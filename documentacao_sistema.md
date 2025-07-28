# Documentação do Sistema de Gestão de Chamados

## Visão Geral

O Sistema de Gestão de Chamados é uma aplicação web desenvolvida para gerenciar tickets de suporte técnico. O sistema permite registrar, visualizar, editar e excluir chamados, além de oferecer um dashboard visual que facilita o acompanhamento do status dos chamados através de um sistema de cores.

## Funcionalidades Principais

### 1. Registro de Chamados
- Formulário completo para cadastro de novos chamados
- Campos editáveis pelo usuário, incluindo número do chamado e data de inclusão
- Validação de dados para garantir integridade das informações

### 2. Dashboard Visual
- Visualização de chamados em cards coloridos por status:
  - **Verde**: Chamados a vencer (data de agendamento futura)
  - **Amarelo**: Chamados vencendo hoje (data de agendamento igual à data atual)
  - **Vermelho**: Chamados atrasados (data de agendamento anterior à data atual)
  - **Azul**: Chamados fechados/resolvidos
- Filtros para visualização específica (todos, vencidos, a vencer, fechados)
- Funcionalidade para marcar chamados como resolvidos diretamente do dashboard

### 3. Gerenciamento de Chamados
- Listagem completa de todos os chamados cadastrados
- Funcionalidades de edição e exclusão de chamados
- Busca e filtros para facilitar a localização de chamados específicos

## Estrutura do Banco de Dados

O sistema utiliza SQLite como banco de dados local, com a seguinte estrutura:

### Tabela: chamados
- **id**: Identificador único (chave primária)
- **numero**: Número do chamado (definido pelo usuário)
- **responsavel**: Nome do responsável pelo chamado
- **empresa**: Nome da empresa relacionada ao chamado
- **descricao**: Descrição detalhada do problema ou solicitação
- **data_inclusao**: Data em que o chamado foi registrado
- **data_agendamento**: Data prevista para atendimento/resolução
- **estado**: Estado atual do chamado (aberto ou fechado)

## Requisitos Técnicos

### Requisitos de Sistema
- Python 3.6 ou superior
- Flask e suas dependências (instaladas via requirements.txt)
- Navegador web moderno (Chrome, Firefox, Edge, Safari)

### Dependências Python
- Flask
- Flask-SQLAlchemy
- Outras dependências listadas no arquivo requirements.txt

## Instalação e Execução

### Passo a Passo para Instalação

1. Extraia o arquivo ZIP em uma pasta de sua preferência
2. Abra o terminal/prompt de comando e navegue até a pasta extraída
3. Crie um ambiente virtual Python:
   ```
   python -m venv venv
   ```
4. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
5. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

### Execução do Sistema

1. Com o ambiente virtual ativado, execute:
   ```
   python -m src.main
   ```
2. Acesse o sistema pelo navegador:
   ```
   http://localhost:5000
   ```

## Guia de Uso

### Registrando um Novo Chamado

1. Acesse a opção "Registrar Chamado" no menu principal
2. Preencha todos os campos do formulário:
   - Número do Chamado: identificador único definido pelo usuário
   - Responsável: pessoa encarregada de resolver o chamado
   - Empresa: organização relacionada ao chamado
   - Descrição: detalhes do problema ou solicitação
   - Data de Inclusão: data em que o chamado está sendo registrado
   - Data de Agendamento: data prevista para resolução
   - Estado: aberto (padrão) ou fechado
3. Clique em "Registrar Chamado"

### Utilizando o Dashboard

1. Acesse a opção "Dashboard" no menu principal
2. Visualize os chamados organizados por cards coloridos
3. Utilize os filtros para visualizar categorias específicas:
   - Todos: exibe todos os chamados
   - Vencidos: exibe apenas chamados atrasados
   - A Vencer: exibe apenas chamados dentro do prazo
   - Fechados: exibe apenas chamados resolvidos
4. Para marcar um chamado como resolvido, clique no botão "Marcar como Resolvido" no card do chamado

### Gerenciando Chamados

1. Acesse a opção "Gerenciar Chamados" no menu principal
2. Visualize a lista completa de chamados
3. Para editar um chamado, clique no botão "Editar" correspondente
4. Para excluir um chamado, clique no botão "Excluir" correspondente

## Solução de Problemas Comuns

### Erro ao iniciar o sistema
- Verifique se o ambiente virtual está ativado
- Confirme se todas as dependências foram instaladas corretamente
- Verifique se não há outro processo utilizando a porta 5000

### Erro ao registrar chamado
- Certifique-se de que todos os campos obrigatórios estão preenchidos
- Verifique se o número do chamado não está duplicado
- Confirme se as datas estão no formato correto (YYYY-MM-DD)

### Problemas de persistência de dados
- Verifique as permissões da pasta onde o banco de dados está armazenado
- Confirme se o banco de dados não está corrompido

## Atualizações e Manutenção

### Backup do Banco de Dados
- O banco de dados SQLite está localizado em `instance/chamados.db`
- Faça backups regulares deste arquivo para evitar perda de dados

### Atualização do Sistema
- Para atualizar o sistema, substitua os arquivos de código-fonte mantendo o arquivo do banco de dados
- Execute `pip install -r requirements.txt` após a atualização para garantir que todas as dependências estejam atualizadas
