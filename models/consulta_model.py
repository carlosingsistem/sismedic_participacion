from database import db
from datetime import datetime
from sqlalchemy import func

class Consulta(db.Model):
    __tablename__ = "consultas"
    
    id_consulta = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    diagnostico = db.Column(db.String(100),nullable=False)
    tratamiento = db.Column(db.String(100), nullable=False)
    id_medico = db.Column(db.Integer, db.ForeignKey('medicos.id_medico'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id_paciente'), nullable=False)
    
    medico = db.relationship("Medico", back_populates="consultas")
    paciente = db.relationship("Paciente", back_populates="consultas")
    
    def __init__(self, fecha, diagnostico, tratamiento, id_medico, id_paciente):
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        
    @staticmethod
    def get_all():
        return Consulta.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Consulta.query.get(id)
    
    @staticmethod
    def get_by_date(fecha_inicio=None, fecha_fin=None):
        query = Consulta.query
        # Si se reciben fechas de inicio y fin, se convierten a formato date
        if fecha_inicio and fecha_fin:
            fecha_inicio_format = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
            fecha_fin_format = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
            #aplicamos un filtro para obtener solo las consultas en ese rango y func.date para convertir esa fecha en el formato date
            query = query.filter(func.date(Consulta.fecha) >= fecha_inicio_format, func.date(Consulta.fecha) <= fecha_fin_format)
            
        return query.order_by(Consulta.fecha).all()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self, fecha=None, diagnostico=None, tratamiento=None, id_medico=None, id_paciente=None):
        if fecha:
            self.fecha = fecha
        if diagnostico:
            self.diagnostico = diagnostico
        if tratamiento:
            self.tratamiento = tratamiento
        if id_medico:    
            self.id_medico = id_medico
        if id_paciente:    
            self.id_paciente = id_paciente
        db.session.commit()        
            
    def delete(self):
        db.session.delete(self)
        db.session.commit()