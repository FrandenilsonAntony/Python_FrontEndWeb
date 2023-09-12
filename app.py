from flask import Flask
app = Flask("Meu App")

@app.route('/')
def hello():
    return "Aplicação em Python com SQLlite.."