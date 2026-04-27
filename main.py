from usuario import login
from arquivo import criar_arquivo, abrir_arquivo, excluir_arquivo, renomear_arquivo, copiar_arquivo, listar_arquivos

# Função de menu para interagir com o usuário
def menu():
    while True:
        print("\nEscolha uma operação:")
        print("1. Criar arquivo")
        print("2. Abrir arquivo")
        print("3. Excluir arquivo")
        print("4. Renomear arquivo")
        print("5. Copiar arquivo")
        print("6. Listar arquivos no diretório")
        print("7. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            nome = input("Digite o nome do arquivo: ")
            criar_arquivo(nome)
        elif escolha == "2":
            nome = input("Digite o nome do arquivo: ")
            abrir_arquivo(nome)
        elif escolha == "3":
            nome = input("Digite o nome do arquivo: ")
            excluir_arquivo(nome)
        elif escolha == "4":
            nome_antigo = input("Digite o nome antigo do arquivo: ")
            nome_novo = input("Digite o novo nome: ")
            renomear_arquivo(nome_antigo, nome_novo)
        elif escolha == "5":
            nome_origem = input("Digite o nome do arquivo de origem: ")
            nome_destino = input("Digite o nome do arquivo de destino: ")
            copiar_arquivo(nome_origem, nome_destino)
        elif escolha == "6":
            diretorio = input("Digite o diretório: ")
            listar_arquivos(diretorio)
        elif escolha == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# Execução
if login():
    menu()