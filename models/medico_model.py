from database import db

class Medico(db.Model):
    __tablename__ = "medicos"
    
    id_medico = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    especialidad = db.Column(db.String(80), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String(120), nullable=False, unique=True)
    # Campo virtual para obtener todas las consultas asociadas a un medico
    consultas = db.relationship("Consulta", back_populates="medico", cascade="all, delete-orphan")
    
    
    def __init__(self, nombre, especialidad, telefono, correo):
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.correo = correo
    # Metodo para guardar el registro de un medico
    def save(self):
        db.session.add(self)
        db.session.commit()
    # Metodo estatico para obtener todos los medicos registrados    
    @staticmethod
    def get_all():
        return Medico.query.all()
    # Metodo estatico para obtenber un registro de un medico por el id
    @staticmethod
    def get_by_id(id):
        return Medico.query.get(id)
    # Metodo actulizar un medico       
    def update(self, nombre=None, especialidad=None, telefono=None, correo=None):
        if nombre:
            self.nombre = nombre
        if especialidad:
            self.especialidad = especialidad
        if telefono:
            self.telefono = telefono
        if correo:
            self.correo = correo
            
        db.session.commit()
    # Metodo para eliminar un medico                  
    def delete(self):
        db.session.delete(self)
        db.session.commit()