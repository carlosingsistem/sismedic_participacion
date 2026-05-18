from flask import render_template

def list_patients(pacientes):
    return render_template("pacientes/index.html", pacientes=pacientes)

def create_patient():
    return render_template("pacientes/create.html")

def edit_patient(paciente):
    return render_template("pacientes/edit.html", paciente=paciente)