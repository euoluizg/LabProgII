def autenticar(usuarios):
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuarios.get(usuario) == senha:
        print("Autenticação bem-sucedida!")
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
        autenticar(usuarios)  # Chama a função novamente para tentar autenticar outra vez