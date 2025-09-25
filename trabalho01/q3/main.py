# Questão 3: Sistema de autenticação simples
# Usuários e senhas pré-definidos. Criar uma função para autenticar.

from autenticacao import autenticar

usuarios = {
    "admin": "1234",
    "joao": "senha123",
    "maria": "abc@2024"
}

autenticar(usuarios)
