import os

BASE = "arquivos_usuario"


def pasta(user):
    path = os.path.join(BASE, user)
    os.makedirs(path, exist_ok=True)
    return path


def criar(user):
    nome = input("Nome arquivo: ")
    conteudo = input("Conteúdo: ")

    with open(os.path.join(pasta(user), nome), "w") as f:
        f.write(conteudo)

    print("Criado!")


def ler(user):
    nome = input("Arquivo: ")

    try:
        with open(os.path.join(pasta(user), nome), "r") as f:
            print("\n--- CONTEÚDO ---")
            print(f.read())
    except:
        print("Erro.")


def editar(user):
    nome = input("Arquivo: ")

    texto = input("Adicionar: ")

    try:
        with open(os.path.join(pasta(user), nome), "a") as f:
            f.write("\n" + texto)
    except:
        print("Erro.")


def excluir(user):
    nome = input("Arquivo: ")

    try:
        os.remove(os.path.join(pasta(user), nome))
        print("Excluído.")
    except:
        print("Erro.")


def listar(user):
    files = os.listdir(pasta(user))

    print("\n--- ARQUIVOS ---")
    for f in files:
        print(f)