# listaContatos= []

# while True:

#     name = input("Digite seu nome: ")

#     idade = int(input("Digite sua idade: "))

#     email = input("Digite seu e-mail: ")

#     contato = {
#         'nome': name,
#         'idade': idade,
#         'email': email
#     }

#     listaContatos.append(contato)

#     print(listaContatos)

users = [
    {
        'email': 'joao@joao.com',
        'password': '1234'
    },
    {
        'email': 'maria@maria.com',
        'password': '1234'
    }
]

while True:
    email: input()
    password: input()

    for user in users:
        if email == user['']