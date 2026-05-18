from flask import render_template

def list_medics(medicos):
    return render_template("medicos/index.html", medicos=medicos)

def create_medic():
    return render_template("medicos/create.html")

def edit_medic(medico):
    return render_template("medicos/edit.html", medico=medico)