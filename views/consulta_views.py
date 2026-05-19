from flask import render_template

def list_consults(consultas):
    return render_template("consultas/index.html" , consultas=consultas)
    
def create_consult(medicos, pacientes):
    return render_template("consultas/create.html", medicos=medicos, pacientes=pacientes)
    
def edit_consult(consulta, medicos, pacientes):
    return render_template("consultas/edit.html", consulta=consulta, medicos=medicos, pacientes=pacientes)