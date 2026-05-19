from flask import request, url_for, redirect, Blueprint
from models.paciente_model import Paciente 
from views import paciente_views

paciente_bp = Blueprint("paciente", __name__, url_prefix="/pacientes")

@paciente_bp.route("/")
def index():
    pacientes = Paciente.get_all()
    return paciente_views.list_patients(pacientes)

@paciente_bp.route("/create" , methods=["GET", "POST"])
def create_patient():
    if request.method == "POST":
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        
        paciente = Paciente(nombre,edad,direccion,telefono)
        paciente.save()
        return redirect(url_for("paciente.index"))
    return paciente_views.create_patient()

@paciente_bp.route("/edit/<int:id_patient>", methods=["GET", "POST"])
def edit_patient(id_patient):
    paciente = Paciente.get_by_id(id_patient)
    if request.method == "POST":
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        
        paciente.update(nombre=nombre, edad=edad, direccion=direccion, telefono=telefono)
        return redirect(url_for("paciente.index"))
    
    return paciente_views.edit_patient(paciente)     

@paciente_bp.route("/delete/<int:id_patient>")
def delete_patient(id_patient):
    paciente = Paciente.get_by_id(id_patient)
    paciente.delete()
    return redirect(url_for("paciente.index"))  

@paciente_bp.route('/historial/<int:id_patient>')
def medical_history(id_patient):
    paciente = Paciente.get_by_id(id_patient)
    consultas = paciente.consultas 
    return paciente_views.medical_history(paciente, consultas)