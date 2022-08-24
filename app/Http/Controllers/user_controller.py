from sqlalchemy.sql import exists
from app.Models.user_model import *
from app.Models.role_model import *
import hashlib
from index import db
from index import ma

def check_login(username, password):
    clave = hashlib.sha256(password.encode('utf-8')).hexdigest()
    existe = User.get(username, clave)
    return existe
def get_data_user(username):
    user = User.get_user_info(username)
    return user
def get_data_role(role_id):
    role = Role.get_role_info(role_id)
    return role