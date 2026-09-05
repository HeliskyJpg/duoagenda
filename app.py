from flask import Flask, render_template
from flask import Flask, render_template, request

USUARIOS = {
    "admin": "1234"
}

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('index.html')


# archivo = open('clientes.txt', 'w') # 'w' = write (crea o sobreescribe)
# archivo.write('Ana Lopez\n')
# archivo.write('Carlos Perez\n')
# archivo.close()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
