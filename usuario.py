import getpass

# Função para login de usuário
def login():
    # Exemplo de dicionário de usuários (login: senha)
    users = {"user1": "senha123", "user2": "senha456"}
    
    # Entrada de dados de login
    username = input("Digite seu nome de usuário: ")
    password = getpass.getpass("Digite sua senha: ")
    
    # Verificando se o usuário e a senha estão corretos
    if username in users and users[username] == password:
        print("Login bem-sucedido!")
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False