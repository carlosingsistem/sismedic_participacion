from flask import request, url_for, redirect, Blueprint
from models.paciente_model import Paciente 
from views import paciente_views

# Creamos el bluprint con nombre paciente y el prefijo pacientes
paciente_bp = Blueprint("paciente", __name__, url_prefix="/pacientes")

# Para listar los pacientes
@paciente_bp.route("/")
def index():
    pacientes = Paciente.get_all()
    return paciente_views.list_patients(pacientes)

# Para crear un paciente
@paciente_bp.route("/create" , methods=["GET", "POST"])
def create_patient():
    if request.method == "POST":
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        # Instanciamos un paciente pasandole los campos requeridos y gaurdamos
        paciente = Paciente(nombre,edad,direccion,telefono)
        paciente.save()
        return redirect(url_for("paciente.index"))
    return paciente_views.create_patient()

# Para editar un paciente mandandole su id
@paciente_bp.route("/edit/<int:id_patient>", methods=["GET", "POST"])
def edit_patient(id_patient):
    paciente = Paciente.get_by_id(id_patient)
    if request.method == "POST":
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        #Realizamos la actulizacion 
        paciente.update(nombre=nombre, edad=edad, direccion=direccion, telefono=telefono)
        return redirect(url_for("paciente.index"))
    
    return paciente_views.edit_patient(paciente)     

#Eliminar un paciente por id
@paciente_bp.route("/delete/<int:id_patient>")
def delete_patient(id_patient):
    paciente = Paciente.get_by_id(id_patient)
    paciente.delete()
    return redirect(url_for("paciente.index"))  

#Para obetner el historial medico del paciente gracias al campo virtual que definimos en el modelo mediante el id
@paciente_bp.route('/historial/<int:id_patient>')
def medical_history(id_patient):
    paciente = Paciente.get_by_id(id_patient)
    consultas = paciente.consultas  #consultas ascociadas al paciente
    return paciente_views.medical_history(paciente, consultas)