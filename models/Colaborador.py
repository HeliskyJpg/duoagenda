import json
from datetime import datetime


class Colaborador:
    def __init__(self, nombre, apellido, fecha_nacimiento, dia_laboral):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.dia_laboral = dia_laboral

    @classmethod
    def cargar_colaboradores(cls):

        with open('models/colaborador.txt', 'r', encoding='utf-8') as f:
            return json.load(f)

    @classmethod
    def agregar_colaborador(cls, nuevo_dict, ruta_archivo="models/colaborador.txt"):
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            datos = []

        datos.append(nuevo_dict)

        # sobreescribe todo
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

    @classmethod
    def calcular_edad(cls,fecha_nacimiento):
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y/%m/%d")

        hoy = datetime.now()

        edad = hoy.year - fecha_nacimiento.year

        return edad

    # resumen_por_dia
    @classmethod
    def all(self):
        data = Colaborador.cargar_colaboradores()
        # print(data)
        
        for n in data:
            # print(n)
            edad = Colaborador.calcular_edad(n["fecha_nacimiento"])
            # print(edad)
            n.update(edad=edad)
            # print(n)
        return data  
      
    def save(self):

        specific_colab = {"nombre": self.nombre, "apellido": self.apellido,
                          "fecha_nacimiento": self.fecha_nacimiento, "dia_laboral": self.dia_laboral}

        Colaborador.agregar_colaborador(specific_colab)
