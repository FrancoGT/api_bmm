import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from sqlalchemy import select
from index import db
from index import ma
from app.Models.role_model import Role
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    lastname = db.Column(db.String(255))

    role_id = db.Column(
        db.Integer,
        db.ForeignKey('role.id', ondelete='CASCADE'),
        nullable=False,
        # no need to add index=True, all FKs have indexes
    )
    role = relationship('Role', backref='role')

    status = db.Column(db.String(1))
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self,username,password,name,lastname,role_id,status):
        self.username = username
        self.password = password
        self.name = name
        self.lastname = lastname
        self.role_id = role_id
        self.status = status
        
    def get(username, password):
        result = User.query.with_entities(User.username==username, User.password==password).first()
        return result == (True,True)
    
    def get_user_info(username):
        result = User.query.filter(User.username==username).first()
        return result

db.create_all()

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields =('id','username','password','name','lastname','role_id','status','created_at','updated_at')
    
user_schema = UserSchema() 
users_schema = UserSchema(many = True)