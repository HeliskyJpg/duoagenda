from models.Colaborador import Colaborador
from flask import Flask, render_template, request, redirect, url_for
from models.forms import RegistrationForm

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template('index.html')


@app.route("/registro", methods=["GET", "POST"])
def registro_colaborador():
    form = RegistrationForm(request.form)
    
    if request.method == "POST":
        if form.validate():
            # Nombre	text	requerido
            # Apellido	text	requerido
            # Fecha de nacimiento	date	requerido
            # Día de la semana que labora
            
            nombre = form.nombre.data
            apellido = form.apellido.data
            fecha_nacimiento = form.fecha_nacimiento.data
            dia_laboral = form.dia.data
            fecha_str = form.fecha_nacimiento.data.strftime('%Y-%m-%d')
            c = Colaborador(nombre, apellido, fecha_str, dia_laboral)

            c.save()

            return redirect(url_for('listado_clientes'))
        
        print(form.errors)
  
    return render_template('registro_agenda.html', form=form)
    


@app.route('/colaboradores')
def listado_clientes():
    data = Colaborador.all()
    return render_template('colaboradores.html', data=data)


@app.route('/resumen')
def listado_resumen():
    data = Colaborador.get_resumen()
    return render_template('resumen.html', data=data)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
