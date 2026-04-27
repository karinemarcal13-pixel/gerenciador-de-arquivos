import tkinter as tk
from usuarios import login, cadastrar

def fazer_login():
    user = entry_user.get()
    senha = entry_senha.get()

    u, tipo = login_simples(user, senha)

    if u:
        status["text"] = f"Bem-vinda {u} ({tipo})"
    else:
        status["text"] = "Login inválido"

def login_simples(user, senha):
    from usuarios import carregar
    usuarios = carregar()

    if user in usuarios and usuarios[user]["senha"] == senha:
        return user, usuarios[user]["tipo"]
    return None, None

# janela
app = tk.Tk()
app.title("Sistema")

tk.Label(app, text="Usuário").pack()
entry_user = tk.Entry(app)
entry_user.pack()

tk.Label(app, text="Senha").pack()
entry_senha = tk.Entry(app, show="*")
entry_senha.pack()

tk.Button(app, text="Login", command=fazer_login).pack()

status = tk.Label(app, text="")
status.pack()

app.mainloop()