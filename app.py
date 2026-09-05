from flask import Flask, render_template
from flask import Flask, render_template, request

USUARIOS = {
    "admin": "1234"
}

app = Flask(__name__)

@app.route("/")
def inicio():
    return 'hola'

# modulo de clientes


if __name__ == "__main__":
    app.run(debug=True, port=5001)
