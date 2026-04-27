from usuarios import login, cadastrar
from sessao import login as set_login, logout
from arquivos import criar, ler, editar, excluir, listar


def menu(user, tipo):

    while True:
        print("\n===== SISTEMA OPERACIONAL =====")
        print(f"Usuário: {user} | Tipo: {tipo}")
        print("1 - Criar arquivo")
        print("2 - Ler arquivo")
        print("3 - Editar arquivo")
        print("4 - Excluir arquivo")
        print("5 - Listar arquivos")

        if tipo == "admin":
            print("6 - Criar usuário")

        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            criar(user)
        elif op == "2":
            ler(user)
        elif op == "3":
            editar(user)
        elif op == "4":
            excluir(user)
        elif op == "5":
            listar(user)
        elif op == "6" and tipo == "admin":
            cadastrar()
        elif op == "0":
            logout()
            break
        else:
            print("Opção inválida!")


# ================= EXECUÇÃO =================

print("1 - Login")
print("2 - Cadastro")

op = input("Escolha: ")

if op == "2":
    cadastrar()

user, tipo = login()

if user:
    set_login(user, tipo)
    menu(user, tipo)