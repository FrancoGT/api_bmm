import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from index import db
from index import ma

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(255))
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(1))
    def __init__(self,nombre,status):
        self.nombre = nombre
        self.status = status

db.create_all()

class RoleSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields =('id','nombre','created_at','updated_at','status')
    
role_schema = RoleSchema()
role_schema = RoleSchema(many = True)