import os
import shutil

# Função para criar um arquivo
def criar_arquivo(nome):
    try:
        with open(nome, 'w') as file:
            file.write("Conteúdo inicial do arquivo.")
        print(f"Arquivo '{nome}' criado.")
    except Exception as e:
        print(f"Erro ao criar o arquivo: {e}")

# Função para abrir e ler o conteúdo de um arquivo
def abrir_arquivo(nome):
    try:
        with open(nome, 'r') as file:
            content = file.read()
        print(f"Conteúdo de {nome}: {content}")
    except FileNotFoundError:
        print(f"O arquivo {nome} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")

# Função para excluir um arquivo
def excluir_arquivo(nome):
    try:
        os.remove(nome)
        print(f"Arquivo '{nome}' excluído.")
    except FileNotFoundError:
        print(f"O arquivo {nome} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao excluir o arquivo: {e}")

# Função para renomear um arquivo
def renomear_arquivo(nome_antigo, nome_novo):
    try:
        os.rename(nome_antigo, nome_novo)
        print(f"Arquivo renomeado de {nome_antigo} para {nome_novo}.")
    except FileNotFoundError:
        print(f"Arquivo {nome_antigo} não encontrado.")
    except Exception as e:
        print(f"Erro ao renomear o arquivo: {e}")

# Função para copiar um arquivo
def copiar_arquivo(nome_origem, nome_destino):
    try:
        shutil.copy(nome_origem, nome_destino)
        print(f"Arquivo '{nome_origem}' copiado para '{nome_destino}'.")
    except FileNotFoundError:
        print(f"Arquivo {nome_origem} não encontrado.")
    except Exception as e:
        print(f"Erro ao copiar o arquivo: {e}")

# Função para listar os arquivos em um diretório
def listar_arquivos(diretorio):
    try:
        arquivos = os.listdir(diretorio)
        print(f"Arquivos em {diretorio}: {arquivos}")
    except FileNotFoundError:
        print(f"O diretório {diretorio} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")