from sqlalchemy.sql import exists
from app.Models.user_model import User
from app.Models.personal_access_token_model import Personal_access_token
import hashlib
from index import db
from index import ma

def check_login(username, password):
        clave = hashlib.sha256(password.encode('utf-8')).hexdigest()
        existe = User.get(username, clave)
        return existe
def registrar_token(token_value):
        tokenable_type = "app/Models/personal_access_token_model"
        tokenable_id = 3
        name = "web"
        token = token_value
        abilities = '["*"]'
        nuevo_token = Personal_access_token(tokenable_type,tokenable_id,name,token,abilities)
        db.session.add(nuevo_token)
        db.session.commit()