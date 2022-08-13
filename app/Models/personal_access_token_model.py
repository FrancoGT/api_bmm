import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
from index import db
from index import ma

class Personal_access_token(db.Model):
    __tablename__ = 'personal_access_tokens'
    id = db.Column(db.Integer, primary_key = True)
    tokenable_type = db.Column(db.String(255))
    tokenable_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    token = db.Column(db.String(64000))
    abilities = db.Column(db.String(64000))
    last_used_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    def __init__(self,tokenable_type,tokenable_id,name,token,abilities):
        self.tokenable_type = tokenable_type
        self.tokenable_id = tokenable_id
        self.name = name
        self.token = token
        self.abilities = abilities

db.create_all()

class Personal_access_tokenSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields =('id','tokenable_type','tokenable_id','name','token','abilities','last_used_at','created_at','updated_at')
    
role_schema = Personal_access_tokenSchema()
role_schema = Personal_access_tokenSchema(many = True)