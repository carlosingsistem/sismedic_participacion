from flask import Flask
from database import db
from controllers import medico_conroller, paciente_controller

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clinica.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(medico_conroller.medico_bp)
app.register_blueprint(paciente_controller.paciente_bp)

@app.route("/")
def home():
    return "<h1>Aplicacion Medic</h1>"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)