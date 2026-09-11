from wtforms import Form, StringField, IntegerField, DateField, validators


class RegistrationForm(Form):
    nombre = StringField('nombre', validators=[validators.Length(
        min=1, max=50), validators.DataRequired()])
    apellido = StringField('apellido', validators=[validators.Length(
        min=1, max=50), validators.DataRequired()])
    fecha_nacimiento = DateField('fecha_nacimiento',
                                 format='%Y-%m-%d',
                                 validators=[validators.DataRequired()
                                             ])
    dia = IntegerField('dia', validators=[
                               validators.DataRequired()])
