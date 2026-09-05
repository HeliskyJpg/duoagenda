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

@app.route("/registro", methods=["GET", "POST"])
def registro_colaborador():
    if request.method =="POST" :
        pass
    else:
        return render_template('registro_agenda.html')
    

# @app.route('/clientes/listado')
# def listado_clientes():
#     with open('clientes.txt', 'r') as f:
#     nombres = [linea.strip() for linea in f] # una lista con cada nombre
#     return render_template('clientes_listado.html', nombres=nombres)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
