import os

ARQ = "dados/users.txt"

def carregar():
    usuarios = {}

    if not os.path.exists(ARQ):
        return usuarios

    with open(ARQ, "r") as f:
        for linha in f:
            user, senha, tipo = linha.strip().split(";")
            usuarios[user] = {"senha": senha, "tipo": tipo}

    return usuarios

def salvar(user, senha, tipo):
    os.makedirs("dados", exist_ok=True)
    with open(ARQ, "a") as f:
        f.write(f"{user};{senha};{tipo}\n")

def cadastrar():
    print("\n=== CADASTRO ===")
    user = input("Novo usuário: ")
    senha = input("Senha: ")
    tipo = input("Tipo (admin/user): ")

    usuarios = carregar()

    if user in usuarios:
        print("Usuário já existe!")
        return None

    salvar(user, senha, tipo)
    print("Usuário criado com sucesso!")
    return user

def login():
    usuarios = carregar()

    print("\n=== LOGIN ===")
    user = input("Usuário: ")
    senha = input("Senha: ")

    if user in usuarios and usuarios[user]["senha"] == senha:
        print("Login ok!")
        return user, usuarios[user]["tipo"]
    else:
        print("Login inválido!")
        return None, None