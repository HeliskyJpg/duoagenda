from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from .models import Colaborador

@app.route("/")
def inicio():
    return render_template('index.html')



@app.route("/registro", methods=["GET", "POST"])
def registro_colaborador():
    if request.method =="POST" :
        # Nombre	text	requerido
        # Apellido	text	requerido
        # Fecha de nacimiento	date	requerido
        # Día de la semana que labora
        nombre = request.form.nombre
        apellido = request.form.apellido
        fecha_nacimiento = request.form.fecha_nacimiento
        dia_laboral = request.form.dia_laboral
        
        c = Colaborador(nombre, apellido,fecha_nacimiento,dia_laboral)
        
        c.save()
        
        return redirect(url_for('listado_clientes'))

    else:
        return render_template('registro_agenda.html')
    

@app.route('/colaboradores')
def listado_clientes():
    data = Colaborador.all()
    return render_template('colaboradores.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
