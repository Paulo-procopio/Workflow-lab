Workflow - Projeto Python com CI/CD

Sobre o Projeto

Este projeto demonstra uma implementação completa de CI/CD (Integração Contínua e Entrega Contínua) usando GitHub Actions. Ele contém funções matemáticas básicas (calculadora) com testes automatizados que rodam a cada push ou pull request.

Funcionalidades

➕ Soma de números
➖ Subtração de números
✖️ Multiplicação de números
➗ Divisão de números (com tratamento de erro para divisão por zero)

Tecnologias Utilizadas

Python 3.10 - Linguagem de programação
pytest - Framework de testes
pytest-cov - Cobertura de testes
GitHub Actions - Automação de CI/CD

Como Funciona
1. Desenvolvimento Local
Você escreve código em src/code.py e testes em teste/test_code.py.
2. Commit e Push
Quando você faz um push para o GitHub:

git add .
git commit -m "Sua mensagem"
git push

3. GitHub Actions em Ação
O GitHub Actions automaticamente:

Cria uma máquina virtual Ubuntu
Clona seu repositório
Instala Python 3.10
Instala as dependências (pytest)
Executa todos os testes
Reporta se passou ou X se falhou



Quando os Testes Rodam
A cada push para qualquer branch
A cada pull request aberto ou atualizado
Manualmente através da aba "Actions" no GitHub
Visualizando os Resultados

Acesse seu repositório no GitHub
Clique na aba "Actions"
Veja todos os workflows executados
Clique em qualquer execução para ver os detalhes