from flask import Flask, render_template, request, session, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pudim'


posts = [
    {
        "titulo":"Minha primeira postagem",
        "texto":"teste"
    },
    {
          "titulo":"Segunda postagem",
          "texto":"Outro teste"
    }

]

@app.route('/')
def exibir_entradas():
    entradas = posts #Mock das postagens
    return render_template('exibir_entradas.html', entradas=entradas)

@app.route('/login', methods=["POST","GET"])
def login():
    erro = None
    if request.method == "POST":
         if request.form['username'] == "admin" and request.form['password'] == "admin":
           session['logado'] = True
           flash("Login efetuado com sucesso!")
           return redirect(url_for('exibir_entradas'))
         erro = "Usuário ou senha inválidos"
    return render_template('login.html', erro=erro)
