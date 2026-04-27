from flask import Flask, render_template, request, redirect
import sqlite3
import os
from database import criar_tabela

app = Flask(__name__)
criar_tabela()

BASE = "arquivos_usuario"

def pasta(user):
    path = os.path.join(BASE, user)
    os.makedirs(path, exist_ok=True)
    return path

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        senha = request.form["senha"]

        conn = sqlite3.connect("sistema.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE user=? AND senha=?", (user, senha))
        result = cursor.fetchone()

        conn.close()

        if result:
            return redirect(f"/dashboard/{user}")

    return render_template("login.html")

@app.route("/dashboard/<user>", methods=["GET", "POST"])
def dashboard(user):
    path = pasta(user)

    if request.method == "POST":
        nome = request.form["nome"]
        conteudo = request.form["conteudo"]

        with open(os.path.join(path, nome), "w") as f:
            f.write(conteudo)

    arquivos = os.listdir(path)
    return render_template("dashboard.html", user=user, arquivos=arquivos)

app.run(debug=True)