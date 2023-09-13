from flask import Flask, render_template

app = Flask(__name__)


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

@app.route('/login')
def login():
    return render_template('login.html')
