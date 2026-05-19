from flask import Blueprint, request, redirect, url_for
from models.consulta_model import Consulta
from models.medico_model import Medico
from models.paciente_model import Paciente 
from views import consulta_views
from datetime import datetime

consulta_bp = Blueprint("consulta", __name__, url_prefix="/consultas")

@consulta_bp.route("/")
def index():
    #consultas=Consulta.get_all()
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')
    consultas = Consulta.get_by_date(fecha_inicio=fecha_inicio,fecha_fin=fecha_fin)
    
    return consulta_views.list_consults(consultas, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)

@consulta_bp.route("/create", methods=["GET", "POST"])
def create_consult():
    if request.method == "POST":
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']
        
        consulta = Consulta(fecha=fecha, diagnostico=diagnostico, tratamiento=tratamiento, id_medico=id_medico, id_paciente=id_paciente)
        consulta.save()
        
        return redirect(url_for("consulta.index"))
    medicos = Medico.get_all()
    pacientes = Paciente.get_all()
    
    return consulta_views.create_consult(medicos, pacientes)

@consulta_bp.route("/edit/<int:id_consult>", methods=["GET", "POST"])
def edit_consult(id_consult):
    consulta = Consulta.get_by_id(id_consult)
    medicos = Medico.get_all()
    pacientes = Paciente.get_all()
    if request.method == "POST":
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']
        
        consulta.update(fecha=fecha, diagnostico=diagnostico, tratamiento=tratamiento, id_medico=id_medico, id_paciente=id_paciente)
        
        return redirect(url_for("consulta.index"))
    
    return consulta_views.edit_consult(consulta, medicos, pacientes)    

@consulta_bp.route("/delete/<int:id_consult>")
def delete_consult(id_consult):
    consulta = Consulta.get_by_id(id_consult)
    consulta.delete()
    return redirect(url_for("consulta.index"))
    