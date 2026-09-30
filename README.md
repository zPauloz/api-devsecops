# 🔐 API DevSecOps

Projeto desenvolvido para praticar conceitos de DevSecOps utilizando Python, Flask e GitHub Actions.

## 🚀 Tecnologias

- Python
- Flask
- Pytest
- Bandit
- pip-audit
- GitHub Actions
- Git

## 📌 Funcionalidades

A aplicação possui dois endpoints:

### Health Check

```text
GET /health

Retorna o status da aplicação.

Página inicial
GET /

Retorna uma mensagem informando que a API está funcionando.

🧪 Testes

Os testes automatizados são executados utilizando Pytest.

pytest
🔒 Segurança

O projeto utiliza:

Bandit

Analisa o código Python procurando possíveis problemas de segurança.

bandit -r . -x ./venv
pip-audit

Verifica as dependências do projeto em busca de vulnerabilidades conhecidas.

pip-audit
⚙️ CI/CD

O GitHub Actions executa automaticamente:

Instalação das dependências
Testes automatizados
Análise de segurança com Bandit
Auditoria das dependências com pip-audit
🎯 Objetivo

Praticar a integração de segurança durante o ciclo de desenvolvimento, aplicando conceitos básicos de DevSecOps em uma API Python.

👨‍💻 Autor

Paulo Henrique Nunes Pereira
