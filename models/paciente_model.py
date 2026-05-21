from database import db

class Paciente(db.Model):
    __tablename__ = "pacientes"
    
    id_paciente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(200))
    telefono = db.Column(db.Integer, nullable=False)
    # Campo virtual para obtener todas las consultas asociadas a un paciente
    consultas = db.relationship("Consulta", back_populates="paciente", cascade="all, delete-orphan")
    
    def __init__(self, nombre, edad, direccion, telefono):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
    # Metodo para guardar el registro de un paciente
    def save(self):
        db.session.add(self)
        db.session.commit()
    # Metodo estatico para obtener todos los registros de los paceintes    
    @staticmethod
    def get_all():
        return Paciente.query.all()
    # Metodo estatico para obtener un registro de un paciente por su id
    @staticmethod
    def get_by_id(id):
        return Paciente.query.get(id)
    # Metodo para actualizar el registro de un paciente
    def update(self, nombre=None, edad=None, direccion=None, telefono=None):
        if nombre:
            self.nombre = nombre
        if edad:
            self.edad = edad
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono
            
        db.session.commit()
    # Metodo para eliminar un paciente de la base de datos        
    def delete(self):
        db.session.delete(self)
        db.session.commit()