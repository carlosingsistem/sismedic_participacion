from flask import request, url_for, redirect, Blueprint
from models.medico_model import Medico 
from views import medico_views
# Creamos el blueprint con nombre medicpo y el prefijo medicos
medico_bp = Blueprint("medico", __name__, url_prefix="/medicos")

# Para listar todos los medicos
@medico_bp.route("/")
def index():
    medicos = Medico.get_all()
    return medico_views.list_medics(medicos)

# Para crear un nuevo medico
@medico_bp.route("/create" , methods=["GET", "POST"])
def create_medic():
    if request.method == "POST":
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        correo = request.form['correo']
        
        medico = Medico(nombre,especialidad,telefono,correo)
        medico.save()
        return redirect(url_for("medico.index"))
    return medico_views.create_medic()

# Para editar un  medico mandandole su id
@medico_bp.route("/edit/<int:id_medico>", methods=["GET", "POST"])
def edit_medic(id_medico):
    medico = Medico.get_by_id(id_medico)
    if request.method == "POST":
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        correo = request.form['correo']
        
        medico.update(nombre=nombre, especialidad=especialidad, telefono=telefono, correo=correo)
        return redirect(url_for("medico.index"))
    
    return medico_views.edit_medic(medico)     

#Eliminar un medico por id
@medico_bp.route("/delete/<int:id_medico>")
def delete_medic(id_medico):
    medico = Medico.get_by_id(id_medico)
    medico.delete()
    return redirect(url_for("medico.index"))  